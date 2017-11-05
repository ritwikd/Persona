"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for additional runserver options.
"""

from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app
from app.commands import InitDbCommand
from os import environ
# from OpenSSL import SSL
#
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('/etc/letsencrypt/live/vps.ritwikd.com/privkey.pem')
# context.use_certificate_chain_file('/etc/letsencrypt/live/vps.ritwikd.com/fullchain.pem')
# context.use_certificate_file('/etc/letsencrypt/live/vps.ritwikd.com/cert.pem')

# Setup Flask-Script with command line commands
manager = Manager(create_app)
manager.add_command('db', MigrateCommand)
manager.add_command('init_db', InitDbCommand)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    #manager.run()
    app = create_app()
    context = ('/etc/letsencrypt/live/vps.ritwikd.com/cert.pem', '/etc/letsencrypt/live/vps.ritwikd.com/privkey.pem')
    app.run(host='0.0.0.0', port=eval(environ.get('PERSONA_PORT')),
            ssl_context=context)
