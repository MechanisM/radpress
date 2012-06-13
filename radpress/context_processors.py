from django.conf import settings
from django.core.urlresolvers import reverse_lazy as reverse
from radpress.settings import DATA as data
from radpress.models import Menu


def context_data(request):
    # add related menu list to data dictionary
    menus = []
    for menu in Menu.objects.filter(page__is_published=True):

        menus.append({
            'url': reverse('radpress-page-detail', args=[menu.page.slug]),
            'title': menu.page.title
        })

    data.update({'RADPRESS_MENUS': menus})
    return data
