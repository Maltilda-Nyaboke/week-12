class Config:
    pass

class TestConfig(Config):
    pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
 Debug = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
