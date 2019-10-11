import os


class Config:
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    DEBUG = True


class DevConfig(Config):
    DEBUG = True
    ENV = 'development'
    MYSQL_HOST = os.environ.get('MY_APP_DB_HOST', '127.0.0.1')
    MYSQL_PORT = os.environ.get('MY_APP_DB_PORT', 3306)
    MYSQL_USER = os.environ.get('MY_APP_DB_USER_NAME', 'root')
    MYSQL_PASSWORD = os.environ.get('MY_APP_DB_USER_PASSWORD', '')
    MYSQL_DB = os.environ.get('MY_APP_DB_NAME', 'Users')
    per_page = 10
    static_url_path = '/static'


def run_config():
    env = os.environ.get("ENV", "DEV")
    if env == "DEV":
        return DevConfig
    else:
        return Config
