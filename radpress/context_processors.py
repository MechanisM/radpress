from radpress import settings


def context_data(request):
    data = {
        'RADPRESS_TITLE': settings.TITLE,
        'RADPRESS_DESCRIPTION': settings.DESCRIPTION,
        'RADPRESS_GA_CODE': settings.GA_CODE
    }

    return data
