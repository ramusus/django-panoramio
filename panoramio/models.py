# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from datetime import datetime
import panoramioapi
import logging

class PanoramioManager(models.GeoManager):

    def near(self, point, radius=None, object=None, set=None, size=None, map_filter=None, limit=None):

        api = panoramioapi.PanoramioAPI()
        logging.debug('Search panoramio photos for object %s' % (object,))
        photos = api.search(lat=point.y, lng=point.x, radius=radius, set=set, size=size, map_filter=map_filter, limit_from=0, limit_to=limit)
        ids = []
        for photo in photos:

            defaults = {
                'photo_id': photo.get('photo_id'),
                'title': photo.get('photo_title'),
                'location': "POINT(%s %s)" % (photo.get('longitude'), photo.get('latitude')),
                'uploaded': datetime.strptime(photo.get('upload_date'), "%d %B %Y"),
                'owner_id': photo.get('owner_id'),
                'owner_name': photo.get('owner_name'),
                'owner_url': photo.get('owner_url'),
            }
            if object:
                defaults.update({
                    'object_id': object.id,
                    'content_type': ContentType.objects.get_for_model(object),
                })

            photo, created = self.get_or_create(photo_id=photo.get('photo_id'), defaults=defaults)
            logging.debug('%s photo "%s" (ID=%d) for object %s' %
                ('Added new' if created else 'Updated', photo.title, photo.photo_id, object))
            ids += [photo.pk]

        return super(PanoramioManager, self).get_query_set().filter(pk__in=ids)
#        return super(PanoramioManager, self).get_query_set().filter(location__distance_lte=(pnt, D(km=kwargs['radius'])))

class Photo(models.Model):
    '''
    Model for panoramio photo image object
    '''
    photo_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=1024)

    location = models.PointField()

    uploaded = models.DateField()
    owner_id = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=50)
    owner_url = models.CharField(max_length=100)

    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType, null=True)
    object = generic.GenericForeignKey()

    objects = PanoramioManager()

    @property
    def photopage_url(self):
        return 'http://www.panoramio.com/photo/%s' % self.photo_id

    @property
    def get_medium_width(self):
        return 500
    @property
    def get_small_width(self):
        return 240
    @property
    def get_thumbnail_width(self):
        return 100
    @property
    def get_square_width(self):
        return 60
    @property
    def get_mini_square_width(self):
        return 32

    @property
    def get_original_url(self):
        return self.photo_file_url_helper('original')
    @property
    def get_medium_url(self):
        return self.photo_file_url_helper('medium')
    @property
    def get_small_url(self):
        return self.photo_file_url_helper('small')
    @property
    def get_thumbnail_url(self):
        return self.photo_file_url_helper('thumbnail')
    @property
    def get_square_url(self):
        return self.photo_file_url_helper('square')
    @property
    def get_mini_square_url(self):
        return self.photo_file_url_helper('mini_square')

    def photo_file_url_helper(self, size):
        return 'http://mw2.google.com/mw-panoramio/photos/%s/%s.jpg' % (size, self.photo_id)

    def __unicode__(self):
        return self.title