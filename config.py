# TODO: Set this up
class Config(object):
    TESTING = False
    DATABASE_URI = ""


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DATABASE_URI = "sqlite:///foo.db"


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


current_config = DevelopmentConfig
current_config_str = "config." + current_config.__name__
