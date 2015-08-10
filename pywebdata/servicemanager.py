import os
import imp
from glob import glob

from baseservice import BaseService
import exceptions as excpt

class ServiceManager(object):

    service_dirs = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'services'))]
    is_initialized = False

    def __init__(self):
        map(self._load_services, self.service_dirs)
        self._set_initialized()

    def _load_services(self, dirname):
        for filename in glob(os.path.join(dirname, '*.py')):
            name, ext = os.path.splitext(filename)
            imp.load_source(name, os.path.join(dirname, filename))

    @classmethod
    def _set_initialized(cls):
        cls.is_initialized = True

    @classmethod
    def add_path(cls, path):
        cls.service_dirs.append(path)

    def activate_service(self, service_name):
        try:
            return BaseService.services[service_name]()
        except:
            raise excpt.ServiceNotFoundException