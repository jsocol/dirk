from django.conf import settings
from django.core.cache import parse_backend_uri

import redis


DEFAULT_BACKEND = 'redis://localhost:6379?db=0'
DEFAULT_PREFIX = 'dirk'


def get_connection():
    uri = getattr(settings, 'DIRK_BACKEND', DEFAULT_BACKEND)
    _, server, params = parse_backend_uri(uri)
    if ':' in server:
        host, _, port = server.partition(':')
        port = int(port)
    else:
        host = server
        port = 6379
    return redis.Redis(host=host,
                       port=port,
                       db=int(params.get('db', 0)),
                       password=params.get('password', None))


def get_prefix():
    return getattr(settings, 'DIRK_PREFIX', DEFAULT_PREFIX)
