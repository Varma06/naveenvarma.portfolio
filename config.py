"""
Flask Configuration Module
Manages environment-specific configurations
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    FLASK_APP = 'app.py'
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    ENV = 'development'
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    ENV = 'production'
    PROPAGATE_EXCEPTIONS = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    ENV = 'testing'


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """Get configuration based on environment"""
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    return config_dict.get(env, DevelopmentConfig)
