from flask import Flask, url_for
from . import config

class Application(Flask):

    def __init__(self, external_uri=None, **kwargs):
        super(Application, self).__init__(__name__)
        self._external_uri = None

        self.config.from_object(config)

    @property
    def external_uri(self):
        return self._external_uri

    @external_uri.setter
    def external_uri(self, value):
        self._external_uri = value

    def run(self, host=None, port=None, debug=None, **options):
        super(Application, self).run(host, port, debug, **options)


app = Application()


