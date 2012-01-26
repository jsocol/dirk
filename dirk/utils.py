from django.conf import settings


DEFAULT_CHANNEL = 'dirk'


def get_channel():
    return getattr(settings, 'DIRK_CHANNEL', DEFAULT_CHANNEL)
