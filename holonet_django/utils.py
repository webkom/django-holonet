from holonet_django import settings


def create_url(*args):
    base_url = settings.holonet_settings.API_URL

    parts = [base_url] + list(args)

    def clean_part(part):
        if str(part).endswith('/'):
            return part[:-1]
        return part

    return ''.join(map(clean_part, parts)) + '/'
