from django.conf import settings
import rasputin

from utils import get_channel


def say(channel, message):
    """Post a message to a dirk channel.

    Dirk channels are mapped to one or more IRC channels.

    """
    data = {
        'channel': channel,
        'message': message
    }
    rasputin.send(get_channel(), data)
