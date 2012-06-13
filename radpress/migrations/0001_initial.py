# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('radpress_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('radpress', ['Tag'])

        # Adding model 'Article'
        db.create_table('radpress_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_body', self.gf('django.db.models.fields.TextField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('radpress', ['Article'])

        # Adding model 'ArticleTag'
        db.create_table('radpress_articletag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radpress.Tag'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radpress.Article'])),
        ))
        db.send_create_signal('radpress', ['ArticleTag'])

        # Adding model 'Page'
        db.create_table('radpress_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_body', self.gf('django.db.models.fields.TextField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('radpress', ['Page'])

        # Adding model 'Menu'
        db.create_table('radpress_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radpress.Page'], unique=True)),
        ))
        db.send_create_signal('radpress', ['Menu'])

        # Adding unique constraint on 'Menu', fields ['order', 'page']
        db.create_unique('radpress_menu', ['order', 'page_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Menu', fields ['order', 'page']
        db.delete_unique('radpress_menu', ['order', 'page_id'])

        # Deleting model 'Tag'
        db.delete_table('radpress_tag')

        # Deleting model 'Article'
        db.delete_table('radpress_article')

        # Deleting model 'ArticleTag'
        db.delete_table('radpress_articletag')

        # Deleting model 'Page'
        db.delete_table('radpress_page')

        # Deleting model 'Menu'
        db.delete_table('radpress_menu')


    models = {
        'radpress.article': {
            'Meta': {'ordering': "('-created_at', '-updated_at')", 'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['radpress.Tag']", 'null': 'True', 'through': "orm['radpress.ArticleTag']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'radpress.articletag': {
            'Meta': {'object_name': 'ArticleTag'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radpress.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radpress.Tag']"})
        },
        'radpress.menu': {
            'Meta': {'unique_together': "(('order', 'page'),)", 'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radpress.Page']", 'unique': 'True'})
        },
        'radpress.page': {
            'Meta': {'ordering': "('-created_at', '-updated_at')", 'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'radpress.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['radpress']