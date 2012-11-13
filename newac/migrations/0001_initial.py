# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visitor'
        db.create_table('newac_visitor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(default='0.0.0.0', max_length=15, db_index=True)),
            ('visit_date', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('ip_map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newac.IPMap'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('newac', ['Visitor'])

        # Adding model 'IPMap'
        db.create_table('newac_ipmap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(default='0.0.0.0', unique=True, max_length=15, db_index=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=4, null=True, blank=True)),
            ('country_name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=64, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=4, blank=True)),
            ('longtitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=4, blank=True)),
            ('latitude_int', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('longtitude_int', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('region_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=64, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('newac', ['IPMap'])

    def backwards(self, orm):
        # Deleting model 'Visitor'
        db.delete_table('newac_visitor')

        # Deleting model 'IPMap'
        db.delete_table('newac_ipmap')

    models = {
        'newac.ipmap': {
            'Meta': {'object_name': 'IPMap'},
            'city_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'unique': 'True', 'max_length': '15', 'db_index': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '4', 'blank': 'True'}),
            'latitude_int': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'longtitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '4', 'blank': 'True'}),
            'longtitude_int': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'newac.visitor': {
            'Meta': {'object_name': 'Visitor'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15', 'db_index': 'True'}),
            'ip_map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['newac.IPMap']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visit_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['newac']