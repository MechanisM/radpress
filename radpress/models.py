from django.db import models
from radpress.templatetags.radpress_tags import restructuredtext


class ArticleManager(models.Manager):

    def all_published(self):
        return self.filter(is_published=True)


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField()
    content_body = models.TextField(editable=False)
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ArticleManager()

    class Meta:
        ordering = ('-created_at', 'updated_at')

    def __unicode__(self):
        return unicode(self.title)

    def save(self, **kwargs):
        self.content_body = restructuredtext(self.content)

        super(Article, self).save(**kwargs)

