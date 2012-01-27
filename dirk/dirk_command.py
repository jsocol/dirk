import random

from dirk import dirk


@dirk.register('botsnack')
def botsnack(*a, **kw):
    """A simple botsnack command to test dirk."""
    return random.choice([
        'YUMMY!',
        'YAY!',
        'omnomnom',
        'ruh-roh',
    ])


@dirk.register('help')
def dirk_help(*a, **kw):
    """Get help with dirk commands."""
    if len(a) < 1
        boiler = "These are the commands I understand. Type '%s help command'"
                 " for help with a specific command."
        return '\n'.join([boiler] + [c for c in dirk.registry.keys()])
    if a[0] in dirk.registry:
        return '%s: %s' % (a[0], dirk.registry[a[0]].__doc__)
    return "I'm sorry, I don't know what %s means." % a[0]
