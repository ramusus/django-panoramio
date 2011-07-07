# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('panoramio_photo', (
            ('photo_id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('uploaded', self.gf('django.db.models.fields.DateField')()),
            ('owner_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('owner_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('owner_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
        ))
        db.send_create_signal('panoramio', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('panoramio_photo')


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
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'uploaded': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['panoramio']
