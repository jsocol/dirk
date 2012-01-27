====
Dirk
====

Dirk, a bastardization of "Django + IRC", is, perhaps obviously, a bridge
between Django and IRC.

Dirk is very much a work-in-progress at this point. Use with caution.


Motivating Example
==================

A long-running Celery task currently requires active monitoring for progress
updates. It would be great if we could get those updates dumped into IRC so we
didn't have to pay such close attention to it!


Architecture
============

The current intersection of the sets of Python Redis clients and Python IRC
client libraries is awful. Ideally, and hopefully eventually, dirk will be
simpler to use.

Dirk is built on Rasputin_, a tool to abstract away multilanguage message
passing via a backend like Redis. On the Django side, you will need to run the
``rasputind`` daemon. You will also need to run a node.js process. These should
probably be on the same machine, as of right now. This allows your Python
processes to send messages via Rasputin (using Redis or other backends) to
node.js, which then echos them into IRC. Or you can initiate messages in IRC
and set up tools to get responses from Django.


Installation
============

Kind of complicated right now. I'm sorry.


Requirements
------------

* Django
* Rasputin_
* Node.js
* Redis


Installing
----------

Add ``rasputin`` and ``dirk`` to ``INSTALLED_APPS``.

Install dirk_ somewhere on the system with NPM. From source, you can do::

    $ git clone https://github.com/jsocol/dirk
    $ cd dirk
    $ npm install .

Installing it globally (``npm install -g dirk``) might be easier.


Configuring
-----------

Configure the Rasputin backend as documented.

Set up ``DIRK_CHANNEL_MAP`` in your Django settings. It's a dict where the keys
are dirk channels (basically any string you want) and the values are lists of
IRC channels, something like::

    DIRK_CHANNEL_MAP = {
        'reindex': ['#sumodev'],
        'new_question': ['#sumo'],
    }


Running
-------

You'll need to run two daemons. Neither (at the moment) daemonizes, so you'll
need to use supervisor_ or screen, or some other trick.

Django::

    $ ./manage.py rasputind

Node (globally installed)::

    $ dirkbot -p /path/to/python -m /path/to/manage.py


Broadcasting
============

To send an unprompted message to IRC, just use the fun ``dirk.say`` command!

::

    from dirk import dirk

    dirk.say('somechannel', 'Hello, world!')

Dirk will send the message via Rasputin to the IRC bot which will, based on the
``DIRK_CHANNEL_MAP`` setting, announce the message in the correct IRC channels.
Boom, simple!

An example might be a status for a long-running process, or a notification from
a cron job, or some rare and special event, like your millionth user
registration.


Receiving and Responding
========================

*NB: Incomplete and Unimplemented*

To make the dirk IRC bot respond with useful information, you'll need to
register a handler for a given command. These will be autodiscovered if they
are in ``dirk_command`` modules of apps in your ``INSTALLED_APPS``.

For example, assuming ``myapp`` is in ``INSTALLED_APPS``, you might have::

    # myapp/dirk_command.py
    from dirk import dirk

    @dirk.register('ping')
    def ping(*args, **kwargs):
        if 'sender' in kwargs:
            return '%s: pong!' % kwargs['sender']
        return 'pong!'

*NB: I have no idea what args or kwargs might be passed to these yet.*

Now, when you restart ``rasputind`` and go back to IRC, you can say to the dirk
bot::

    <james> dirkbot: ping
    <dirkbot> james: pong!

Or you can ``/msg`` the dirk bot::

    to dirkbot: ping
    from dirkbot: pong!


TODO
====

There's still quite a lot to do. Grep 'TODO' and you'll see.


.. _Rasputin: http://rasputinproject.org
.. _supervisor: http://supervisord.org/
.. _dirk: https://github.com/jsocol/dirk
