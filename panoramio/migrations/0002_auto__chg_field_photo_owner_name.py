# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Photo.owner_name'
        db.alter_column('panoramio_photo', 'owner_name', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'Photo.owner_name'
        db.alter_column('panoramio_photo', 'owner_name', self.gf('django.db.models.fields.CharField')(max_length=50))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'panoramio.photo': {
            'Meta': {'object_name': 'Photo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'owner_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'uploaded': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['panoramio']
