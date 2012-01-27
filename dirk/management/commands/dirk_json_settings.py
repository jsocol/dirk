import json

from django.conf import settings
from django.core.management.base import NoArgsCommand

from dirk.utils import get_node_settings


class Command(NoArgsCommand):
    help = 'Dumps dirk settings for the IRC bot.'

    def handle_noargs(self, *a, **kw):
        print json.dumps(get_node_settings())
