import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer
from radpress.templatetags.radpress_tags import restructuredtext
from radpress.settings import MORE_TAG


class ThumbnailModelMixin(object):
    def get_thumbnail(self, path, size):
        thumbnailer = get_thumbnailer(path)
        thumb = thumbnailer.get_thumbnail({'size': size, 'crop': True})

        return thumb

    def get_thumbnail_tag(self, image, size=None):
        size = size or (50, 50)
        thumb = self.get_thumbnail(image.path, size)
        url = thumb.url.replace(
            '%s/' % settings.MEDIA_ROOT, settings.MEDIA_URL)
        res = '<a href="%s" target="_blank"><img src="%s" height="%s" /></a>'

        return res % (image.url, url, size[1])


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return unicode(self.name)


class EntryImage(ThumbnailModelMixin, models.Model):
    name = models.CharField(
        max_length=100, blank=True,
        help_text=_("A simple description about image."))
    image = models.ImageField(upload_to='radpress/entry_images/')

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __unicode__(self):
        image_name = os.path.split(self.image.name)[1]
        return u"%s - %s" % (self.name, image_name)

    def thumbnail_tag(self):
        if not self.image:
            return ''

        return self.get_thumbnail_tag(self.image)

    thumbnail_tag.allow_tags = True
    thumbnail_tag.short_description = ''


class EntryManager(models.Manager):

    def all_published(self):
        return self.filter(is_published=True)


class Entry(models.Model):
    """
    Radpress' main model. It includes articles to show in Radpress mainpage.
    The content body is auto filled by content value after it converted to html
    from restructuredtext. And it has `is_published` to avoid viewing in blog
    list page.

    The `created_at` is set datetime information automatically when a 'new'
    blog entry saved, but `updated_at` will be updated in each save method ran.
    """
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    content_body = models.TextField(editable=False)
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EntryManager()

    class Meta:
        abstract = True
        ordering = ('-created_at', '-updated_at')

    def __unicode__(self):
        return unicode(self.title)

    def save(self, **kwargs):
        self.content_body = restructuredtext(self.content)

        super(Entry, self).save(**kwargs)


class Article(Entry):
    cover_image = models.ForeignKey(EntryImage, blank=True, null=True)
    tags = models.ManyToManyField(
        Tag, null=True, blank=True, through='ArticleTag')

    @property
    def content_by_more(self):
        content_list = self.content_body.split(MORE_TAG, 1)
        content = content_list[0]

        if len(content_list) > 1:
            content = content.strip() + '</div>'

        return content


class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return u"%s - %s" % (self.tag.name, self.article)


class Page(Entry):
    pass


class Menu(models.Model):
    order = models.PositiveSmallIntegerField(default=3)
    page = models.ForeignKey(Page, unique=True)

    class Meta:
        unique_together = ('order', 'page')

    def __unicode__(self):
        return u'%s - %s' % (self.order, self.page.title)
