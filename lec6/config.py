import os

class Config:
    SECRET_KEY = 'my-secret-key' or os.environ.get('SECRET_KEY')