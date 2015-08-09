from servicemanager import ServiceManager

service_manager = ServiceManager()

class Service(object):

    def __init__(self, service_string):
        
        self.service = service_manager.activate_service(service_string)
        print self.service

    def query(self, *args, **kwargs):
        self.service.query(*args, **kwargs)