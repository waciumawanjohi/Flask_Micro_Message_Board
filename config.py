import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "the_longest_passwords_you_know"
