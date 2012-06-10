# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArticleTag'
        db.create_table('radpress_articletag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radpress.Tag'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radpress.Article'])),
        ))
        db.send_create_signal('radpress', ['ArticleTag'])


        # Changing field 'Page.title'
        db.alter_column('radpress_page', 'title', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Article.title'
        db.alter_column('radpress_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=500))
        # Removing M2M table for field tags on 'Article'
        db.delete_table('radpress_article_tags')


    def backwards(self, orm):
        # Deleting model 'ArticleTag'
        db.delete_table('radpress_articletag')


        # Changing field 'Page.title'
        db.alter_column('radpress_page', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Article.title'
        db.alter_column('radpress_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding M2M table for field tags on 'Article'
        db.create_table('radpress_article_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['radpress.article'], null=False)),
            ('tag', models.ForeignKey(orm['radpress.tag'], null=False))
        ))
        db.create_unique('radpress_article_tags', ['article_id', 'tag_id'])


    models = {
        'radpress.article': {
            'Meta': {'ordering': "('-created_at', 'updated_at')", 'object_name': 'Article'},
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
            'Meta': {'unique_together': "(('setting', 'order', 'page'),)", 'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radpress.Page']", 'unique': 'True'}),
            'setting': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radpress.Setting']"})
        },
        'radpress.page': {
            'Meta': {'ordering': "('-created_at', 'updated_at')", 'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'radpress.setting': {
            'Meta': {'object_name': 'Setting'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'ga_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'radpress.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['radpress']