from django.conf import settings

DATA = {
    'RADPRESS_TITLE': getattr(settings, 'RADPRESS_TITLE', "Radpress"),
    'RADPRESS_DESCRIPTION': getattr(
        settings, 'RADPRESS_DESCRIPTION',
        "A blogging application for Djangonauts"),
    'RADPRESS_LIMIT': getattr(settings, 'RADPRESS_LIMIT', 5),
    'RADPRESS_GA_CODE': getattr(settings, 'RADPRESS_GA_CODE', None),
    'RADPRESS_DISQUS': getattr(settings, 'RADPRESS_DISQUS', None),
    'RADPRESS_COVER_SIZE': getattr(settings, 'RADPRESS_COVER_SIZE', '652x248')
}

MORE_TAG = '<!-- more -->'
