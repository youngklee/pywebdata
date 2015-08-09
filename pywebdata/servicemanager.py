import os
import imp
import glob
import pkgutil

from baseservice import BaseService
from exceptions import ServiceNotFoundException

class ServiceManager(object):

    service_dir = os.path.join(os.path.dirname(__file__), 'services')
    service_dirs = [service_dir]

    def __init__(self):
        map(self._load_services, self.service_dirs)
        
    def _load_services(self, dirname):
        for filename in glob.glob(os.path.join(dirname, '*.py')):
            name, ext = os.path.splitext(filename)
            imp.load_source(name, os.path.join(dirname, filename))

    @classmethod
    def add_path(cls, path):
        cls.service_dirs.append(path)

    def activate_service(self, service_name):
        try:
            return BaseService.services[service_name]()
        except:
            raise ServiceNotFoundException