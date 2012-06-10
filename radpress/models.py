from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from radpress.templatetags.radpress_tags import restructuredtext


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return unicode(self.name)


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
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    content_body = models.TextField(editable=False)
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EntryManager()

    class Meta:
        abstract = True
        ordering = ('-created_at', 'updated_at')

    def __unicode__(self):
        return unicode(self.title)

    def save(self, **kwargs):
        self.content_body = restructuredtext(self.content)

        super(Entry, self).save(**kwargs)


class Article(Entry):
    tags = models.ManyToManyField(
        Tag, null=True, blank=True, through='ArticleTag')


class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return u"%s - %s" % (self.tag.name, self.article)


class Page(Entry):
    pass


class SettingManager(models.Manager):

    def get_current_settings(self):
        site = Site.objects.get(id=settings.SITE_ID)
        (setting, is_created) = self.get_or_create(site=site)

        if is_created:
            setting.title = 'Radpress'
            setting.description = "A blogging application for Djangonauts."
            setting.save()

        return setting

    def get_current_settings_dict(self):
        data = {}
        prefix = 'RADPRESS'

        # get settings
        settings_dict = self.values().get(site__id=settings.SITE_ID)
        for setting in settings_dict:
            if setting.endswith('id'):
                continue

            data_key = '%s_%s' % (prefix, setting.upper())
            data_value = settings_dict.get(setting)
            data.update({data_key: data_value})

        # add related menu list to data dictionary
        menus = []
        for menu in Menu.objects.filter(
            setting__site__id=settings.SITE_ID, page__is_published=True):

            menus.append({
                'url': reverse('radpress-page-detail', args=[menu.page.slug]),
                'title': menu.page.title
            })

        data.update({'%s_MENUS' % prefix: menus})

        return data


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


class Menu(models.Model):
    setting = models.ForeignKey(Setting)
    order = models.PositiveSmallIntegerField(default=3)
    page = models.ForeignKey(Page, unique=True)

    class Meta:
        unique_together = ('setting', 'order', 'page')

    def __unicode__(self):
        return u'%s - %s' % (self.order, self.page.title)
