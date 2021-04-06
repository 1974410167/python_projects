

def get_db_uri(dbinfo):

    engine = dbinfo.get('ENGINE')
    driver = dbinfo.get('DRIVER')
    user = dbinfo.get('USER')
    password = dbinfo.get('PASSWORD')
    host = dbinfo.get('HOST')
    port = dbinfo.get('PORT')
    name = dbinfo.get('NAME')

    return f'{engine}+{driver}://{user}:{password}@{host}:{port}/{name}'
class Config:

    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'loaclhost',
        'PORT':'3306',
        'NAME':'',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)