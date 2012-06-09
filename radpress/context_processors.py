from radpress.models import Setting


def context_data(request):
    return Setting.objects.get_current_settings_dict()
