import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25


    MAIL_SERVER='localhost'
    MAIL_PORT=8025

    #python -m smtpd -n -c DebuggingServer localhost:8025


    ADMINS = ['evgeny_vlasov@yahoo.com']

    # MAIL_SERVER = 'smtp.sendgrid.net'
    # MAIL_USERNAME = 'apikey'
    # MAIL_PASSWORD = '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'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
