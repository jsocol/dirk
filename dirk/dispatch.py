"""Dirk's rasputin event handlers."""
from rasputin import register

from . import dirk
from .utils import get_rasputin_channel


_handlers_loaded = False


def autodiscover():
    global _handlers_loaded
    if _handlers_loaded:
        return
    _handlers_loaded = True


autodiscover()


@register.channel(get_rasputin_channel() + '-in')
def dirk_dispatcher(data):
    """Dispatches rasputin messages to dirk handlers and sends the result back.

    Rasputin is fundamentally one-way, so here we abstract over that to allow
    for two-way commmunication between Django and IRC.

    The node.js side of dirk sends the messages via rasputin to the Django
    rasputin daemon, where this handler finds them, dispatches them again to
    the correct dirk handlers. Dirk handlers are allowed, and expected, to
    return a value, which this dispatcher then sends back, with some
    appropriate metadata, to node.js, which echos them back to the correct
    target.

    """
    # TODO(james): Autodiscover dirk handlers.
    # TODO(james): Implement.
    raise NotImplemented

    # Send the message back to the dirk node.js process.
    channel, message = something()
    dirk.say(channel, message)
