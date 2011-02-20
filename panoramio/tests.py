# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.gis.geos import Point
from models import Photo

class PanoramioTest(TestCase):

    def test_searching_photos(self):
        '''
        Test for searching and saving found photos
        '''
        photos = Photo.objects.near(point=Point(-4.291191, 55.872205), limit=7)
        self.assertEqual(len(photos), 7)
        self.assertEqual(Photo.objects.count(), 7)