from django.conf import settings
import rasputin

from utils import get_rasputin_channel, get_channel_map


def say(channel, message):
    """Post a message to a dirk channel.

    Dirk channels are mapped to one or more IRC channels by the
    DIRK_CHANNEL_MAP setting.

    """
    map_ = get_channel_map()
    irc_channels = map_.get(channel, [])
    data = {
        'channels': irc_channels,
        'message': message
    }
    rasputin.send(get_rasputin_channel(), data)


class AlreadyRegistered(Exception):
    pass


registry = {}


def register(command):
    """Register a dirk command handler."""
    if command in registry:
        raise AlreadyRegistered('%s is already a registered command' % command)

    def _decorator(f):
        registry[command] = f
        return f
    return _decorator
