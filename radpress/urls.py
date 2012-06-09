from django.conf.urls import patterns, url
from radpress.views import Archive, Detail, Index, Preview, PageDetail
from radpress.feeds import ArticleFeed

urlpatterns = patterns(
    '',

    url(r'^$',
        view=Index.as_view(),
        name='radpress-index'),

    url(r'^archives/$',
        view=Archive.as_view(),
        name='radpress-archive'),

    url(r'^detail/(?P<slug>[-\w]+)/$',
        view=Detail.as_view(),
        name='radpress-detail'),

    url(r'^p/(?P<slug>[-\w]+)/$',
        view=PageDetail.as_view(),
        name='radpress-page-detail'),

    url(r'^preview/$',
        view=Preview.as_view(),
        name='radpress-preview'),

    url(r'^rss/$',
        view=ArticleFeed(),
        name='radpress-rss'),

    url(r'^rss/(?P<tags>[-/\w]+)/$',
        view=ArticleFeed(),
        name='radpress-rss')
)
