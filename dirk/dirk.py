from django.conf import settings

from utils import get_connection, get_prefix


def say(channel, message):
    conn = get_connection()
    pub = '.'.join((get_prefix(), channel))
    conn.publish(pub, message)
