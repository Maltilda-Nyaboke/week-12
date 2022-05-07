class Config:
    pass


class ProdConfig(Config):
    pass

class DevConfig(Config):
 Debug = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
