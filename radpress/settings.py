from django.conf import settings

TITLE = getattr(settings, 'RADPRESS_TITLE', 'RADPRESS')
DESCRIPTION = getattr(
    settings, 'RADPRESS_DESCRIPTION', 'Simple django blog engine.')
GA_CODE = getattr(settings, 'RADPRESS_GA_CODE', None)
