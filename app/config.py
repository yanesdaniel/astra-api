class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True


config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig
}