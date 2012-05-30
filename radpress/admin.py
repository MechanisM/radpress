from django.contrib import admin
from radpress.models import Article, Setting
from radpress.forms import ArticleForm


class MarkupAdminMixin(object):

    class Media:
        css = {
            'all': (
                'radpress/markitup/skins/simple/style.css',
                'radpress/markitup/sets/rest/style.css')
        }
        js = (
            'radpress/markitup/jquery.markitup.js',
            'radpress/markitup/sets/rest/set.js')


class ArticleAdmin(admin.ModelAdmin, MarkupAdminMixin):

    list_display = ['title', 'created_at', 'updated_at', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)


class SettingAdmin(admin.ModelAdmin):

    list_display = ['site', 'title']

admin.site.register(Setting, SettingAdmin)
