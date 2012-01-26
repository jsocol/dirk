from django.conf import settings


DEFAULT_RASPUTIN = 'dirk'


def get_channel_map():
    return getattr(settings, 'DIRK_CHANNEL_MAP', {})


def get_rasputin_channel():
    return getattr(settings, 'DIRK_RASPUTIN_CHANNEL', DEFAULT_RASPUTIN)
