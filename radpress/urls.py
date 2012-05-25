from django.conf.urls import patterns, url
from radpress.views import Index

urlpatterns = patterns(
    '',

    url(r'^$',
        view=Index.as_view(),
        name='radpress-index')
)
