from django.contrib import admin
from radpress.models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'created_at', 'updated_at', 'is_published']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
