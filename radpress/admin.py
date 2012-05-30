from django.contrib import admin
from radpress.models import Article, Setting, Page
from radpress.forms import ArticleForm, PageForm


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


class EntryAdmin(admin.ModelAdmin, MarkupAdminMixin):
    list_display = ['title', 'created_at', 'updated_at', 'is_published']
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(EntryAdmin):
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)


class PageAdmin(EntryAdmin):
    form = PageForm

admin.site.register(Page, PageAdmin)


class SettingAdmin(admin.ModelAdmin):
    list_display = ['site', 'title']

admin.site.register(Setting, SettingAdmin)
