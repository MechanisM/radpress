from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from radpress.templatetags.radpress_tags import restructuredtext


class ArticleManager(models.Manager):

    def all_published(self):
        return self.filter(is_published=True)


class Article(models.Model):
    """
    Radpress' main model. It includes articles to show in Radpress mainpage.
    The content body is auto filled by content value after it converted to html
    from restructuredtext. And it has `is_published` to avoid viewing in blog
    list page.

    The `created_at` is set datetime information automatically when a 'new'
    blog entry saved, but `updated_at` will be updated in each save method ran.
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
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


class SettingManager(models.Manager):

    def get_current_settings(self):
        return self.values().get(site__id=settings.SITE_ID)


class Setting(models.Model):
    site = models.OneToOneField(Site)
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=256, blank=True)
    ga_code = models.CharField(
        max_length=32, blank=True,
        help_text=_("Google Analytics Code. It should start with 'UA-'."))

    objects = SettingManager()

    def __unicode__(self):
        return unicode(self.site)
