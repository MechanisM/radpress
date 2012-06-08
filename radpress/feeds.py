from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from radpress.models import Article, Setting


class ArticleFeed(Feed):

    def __init__(self):
        settings = Setting.objects.get_current_settings()
        self.title = settings.title
        self.description = settings.description
        self.link = reverse_lazy('radpress-index')

    def get_object(self, request):
        objects = Article.objects.filter(is_published=True)

        return objects

    def items(self, obj):
        return obj

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse_lazy('radpress-detail', args=[item.slug])

    def item_pubdate(self, item):
        return item.created_at

    def item_description(self, item):
        return item.content_body
