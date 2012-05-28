from django.conf.urls import patterns, url
from radpress.views import Index, Preview

urlpatterns = patterns(
    '',

    url(r'^$',
        view=Index.as_view(),
        name='radpress-index'),

    url(r'^preview/$',
        view=Preview.as_view(),
        name='radpress-preview')
)
