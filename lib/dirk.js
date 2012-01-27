var Rasputin = require('rasputin').Rasputin,
    irc = require('irc'),
    options = require('nomnom').opts({
        python: {
            string: '-p PYTHON, --python=PYTHON',
            default: '/usr/bin/python',
            help: 'Path to the Python executable.'
        },
        manage: {
            string: '-m MANAGEPY, --manage=MANAGEPY',
            required: true,
            help: "Path to Django's manage.py."
        }
    }).parseArgs();
    child = require('child_process');


function main(config) {
    // TODO(james): Pass connection options.
    var rasputin = new Rasputin();
    var client = new irc.Client(config.host, config.nick, {
            channels: config.channels
        });
    client.on('error', function(err) {
        if (err.rawCommand != '421') {
            console.log(err);
            if (err.hasOwnProperty('stack')) {
                console.log(err.stack);
            }
        }
    });

    // TODO(james): Find a way to accept messages and pass them back to
    // Rasputin.

    rasputin.on(config.channel, function(_, data) {
        // Decide which channels to send the message to.
        data.channels.forEach(function(c) {
            client.say(c, data.message);
        });
    });
}

var exec = options.python + ' ' + options.manage + ' ';
child.exec(exec + 'dirk_json_settings', function(err, stdout, stderr) {
    if (err) {
        console.log(err);
        process.exit(1);
    }
    var config = JSON.parse(stdout);
    main(config);
});
