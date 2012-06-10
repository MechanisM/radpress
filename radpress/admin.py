from django.contrib import admin
from radpress.models import Article, ArticleTag, Menu, Page, Setting, Tag
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


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1


class ArticleAdmin(EntryAdmin):
    form = ArticleForm
    inlines = [ArticleTagInline]

    def tag_list(self, obj):
        tag_list = [tag.name for tag in obj.tags.all()]

        return ', '.join(tag_list)

    def get_list_display(self, request):
        list_display = super(ArticleAdmin, self).get_list_display(request)
        if not 'tag_list' in list_display:
            list_display.insert(3, 'tag_list')

        return list_display

admin.site.register(Article, ArticleAdmin)


class PageAdmin(EntryAdmin):
    form = PageForm

admin.site.register(Page, PageAdmin)


class MenuInline(admin.TabularInline):
    model = Menu
    max_num = 5
    extra = 5


class SettingAdmin(admin.ModelAdmin):
    list_display = ['site', 'title']
    inlines = [MenuInline]

admin.site.register(Setting, SettingAdmin)


class TagAdmin(admin.ModelAdmin):

    def articles(self, obj):
        return obj.article_set.count()

    list_display = ['name', 'slug', 'articles']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)
