# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MathEngineHistory'
        db.create_table(u'math_engine_mathenginehistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('values', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sum', self.gf('django.db.models.fields.IntegerField')()),
            ('product', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'math_engine', ['MathEngineHistory'])


    def backwards(self, orm):
        # Deleting model 'MathEngineHistory'
        db.delete_table(u'math_engine_mathenginehistory')


    models = {
        u'math_engine.mathenginehistory': {
            'Meta': {'object_name': 'MathEngineHistory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'product': ('django.db.models.fields.IntegerField', [], {}),
            'sum': ('django.db.models.fields.IntegerField', [], {}),
            'values': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['math_engine']