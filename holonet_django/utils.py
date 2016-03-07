import django

from holonet_django import settings


def create_url(*args, **kwargs):
    base_url = settings.holonet_settings.API_URL

    base_parts = [base_url]
    if kwargs.get('api_path', True):
        base_parts.append('/api/')

    parts = base_parts + list(args)

    def clean_part(part):
        if str(part).endswith('/'):
            return part[:-1]
        return part

    return ''.join(map(clean_part, parts)) + '/'


def get_model(*args):
    if django.VERSION >= (1, 7):
        from django.apps import apps
        model = apps.get_model(app_label=args[0], model_name=args[1])
        return model
    else:
        from django.db.models import get_model
        model = get_model(*args)
        return model
