
class ServiceMount(type):

    def __init__(self, name, bases, attrs):
        if not hasattr(self, 'services'):
            self.services = {}
        else:
            self.services[self.name] = self

class BaseService(object):

    __metaclass__ = ServiceMount

    def query(self, *args, **kwargs):
        raise NotImplementedError