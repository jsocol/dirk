from django.conf import settings


DEFAULT_RASPUTIN = 'dirk'
DEFAULT_IRC_HOST = 'chat.freenode.net'
DEFAULT_IRC_NICK = 'dirkbot'


def get_channel_map():
    return getattr(settings, 'DIRK_CHANNEL_MAP', {})


def get_rasputin_channel():
    return getattr(settings, 'DIRK_RASPUTIN_CHANNEL', DEFAULT_RASPUTIN)


def get_node_settings():
    node = {
        'irc_host': getattr(settings, 'DIRK_IRC_HOST', DEFAULT_IRC_HOST),
        'irc_nick': getattr(settings, 'DIRK_IRC_NICK', DEFAULT_IRC_NICK),
        'channels': get_channel_map().keys(),
        'rasputin_host': getattr(settings, 'RASPUTIN_HOST', 'localhost'),
        'rasputin_port': getattr(settings, 'RASPUTIN_PORT', 6379),
        'rasputin_password': getattr(settings, 'RASPUTIN_PASSWORD', None),
        'rasputin_db': getattr(settings, 'RASPUTIN_REDIS_DB', 0),
        'rasputin_channel': get_rasputin_channel(),
    }
    return node
