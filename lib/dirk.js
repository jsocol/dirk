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
    var rasputin = new Rasputin({
            'host': config.rasputin_host,
            'port': config.rasputin_port
        });
    var client = new irc.Client(config.irc_host, config.irc_nick, {
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

    var to_me = new RegExp('^' + config.irc_nick + ':\\s+');
    console.log(to_me);
    client.on('message', function(from, to, msg) {
        // TODO: Private messaging.
        console.log([from, to, msg]);
        if (!to_me.test(msg)) { return; }
        msg = msg.replace(to_me, '');
        console.log(msg);
        var data = {
                'from': from,
                'to': to,
                'msg': msg
            };
        rasputin.send(config.rasputin_in_channel, data);
    });

    rasputin.on(config.rasputin_channel, function(_, data) {
        // Decide which channels to send the message to.
        console.log(data);
        data.channels.forEach(function(c) {
            client.say(c, data.message);
        });
    }).run();
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
