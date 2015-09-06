import os
import imp
from glob import glob

from baseservice import BaseService
import exceptions as excpt

class ServiceManager(object):

    service_dirs = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'services'))]
    is_initialized = False

    @classmethod
    def load_all(cls):
        map(cls.load_from_directory, cls.service_dirs)
        cls._set_initialized()

    @staticmethod
    def load_from_directory(dirname):
        for filename in glob(os.path.join(dirname, '*.py')):
            imp.load_source('pywebdata', os.path.join(dirname, filename))

    @classmethod
    def _set_initialized(cls):
        cls.is_initialized = True

    @classmethod
    def register_path(cls, path):
        if not cls.is_initialized:
            cls.service_dirs.append(path)
        else:
            raise excpt.ServiceManagerInitializedException

    @staticmethod
    def fetch_service(service_name):

        if service_name not in BaseService.services.keys():
            raise excpt.ServiceNotFoundException

        return BaseService.services[service_name]()

    @staticmethod
    def get_services():
        return BaseService.services.keys()
        