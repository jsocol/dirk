import json

from django.conf import settings
from django.core.management.base import NoArgsCommand

from dirk.utils import get_rasputin_channel, get_channel_map


class Command(NoArgsCommand):
    help = 'Dumps dirk settings for the IRC bot.'

    def handle_noargs(self, *a, **kw):
        # TODO(james): Dump Redis connection info.
        print json.dumps({
            'channel': get_rasputin_channel(),
            'map': get_channel_map(),
        })
