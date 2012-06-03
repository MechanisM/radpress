from django import forms
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from radpress.models import Entry, Page


class MarkupWidget(forms.Textarea):

    def render(self, name, value, attrs=None):
        html = super(MarkupWidget, self).render(name, value, attrs)
        html += """
            <script type="text/javascript">
                (function($) {
                    restSettings.previewParserPath = '%s';
                    $('textarea').markItUp(restSettings);
                })(django.jQuery);
            </script>
        """ % reverse('radpress-preview')

        return mark_safe(html)


class EntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

        # change content widget.
        content = self.fields.get('content')
        content.widget = MarkupWidget()


class ArticleForm(EntryForm):

    class Meta:
        model = Entry


class PageForm(EntryForm):

    class Meta:
        model = Page
