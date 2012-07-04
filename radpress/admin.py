from django.contrib import admin
from radpress.models import Article, ArticleTag, EntryImage, Menu, Page, Tag
from radpress.forms import ArticleForm, PageForm


def toggle_published(modeladmin, request, queryset):
    for obj in queryset:
        obj.is_published = not obj.is_published
        obj.save()

toggle_published.short_description = "Change published status of the article"


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
    list_filter = ('is_published',)
    search_fields = ('title',)
    actions = [toggle_published]


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1


class ArticleAdmin(EntryAdmin):
    form = ArticleForm
    inlines = [ArticleTagInline]
    list_display = (
        'title', 'created_at', 'updated_at', 'tag_list', 'is_published')
    list_filter = ('is_published', 'tags')

    def tag_list(self, obj):
        tag_list = [tag.name for tag in obj.tags.all()]

        return ', '.join(tag_list)

admin.site.register(Article, ArticleAdmin)


class PageAdmin(EntryAdmin):
    form = PageForm

admin.site.register(Page, PageAdmin)


class TagAdmin(admin.ModelAdmin):

    def articles(self, obj):
        return obj.article_set.count()

    list_display = ['name', 'slug', 'articles']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)
admin.site.register(Menu, admin.ModelAdmin)


class EntryImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', '__unicode__', 'name')
    list_display_links = ('__unicode__',)
    search_fields = ('image', 'name')

admin.site.register(EntryImage, EntryImageAdmin)
