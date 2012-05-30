from radpress.settings import DEFAULT_SETTINGS
from radpress.models import Setting


def context_data(request):
    data = {}
    current_settings = Setting.objects.get_current_settings()
    for setting in current_settings:
        if setting.endswith('id'):
           continue

        data_key = 'RADPRESS_%s' % setting.upper()
        data_value = current_settings.get(setting)
        if not data_value:
            data_value = DEFAULT_SETTINGS.get(setting)

        data.update({data_key: data_value})

    return data
