from django.conf.urls import patterns, url
from radpress.views import Detail, Index, Preview

urlpatterns = patterns(
    '',

    url(r'^$',
        view=Index.as_view(),
        name='radpress-index'),

    url(r'^detail/(?P<slug>[-\w]+)/$',
        view=Detail.as_view(),
        name='radpress-detail'),

    url(r'^preview/$',
        view=Preview.as_view(),
        name='radpress-preview'),
)
