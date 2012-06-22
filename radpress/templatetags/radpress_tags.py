from django import template
from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from docutils.core import publish_parts
from docutils.parsers.rst import directives
from radpress.rst_directives import Pygments, More

register = template.Library()


@register.filter
def restructuredtext(value):
    docutils_settings = getattr(
        settings, 'RESTRUCTUREDTEXT_FILTER_SETTINGS', {})
    parts = publish_parts(
        source=smart_str(value), writer_name="html",
        settings_overrides=docutils_settings)

    return mark_safe(force_unicode(parts['html_body']))

restructuredtext.is_safe = True
directives.register_directive('sourcecode', Pygments)
directives.register_directive('more', More)
