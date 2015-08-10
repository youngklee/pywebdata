from servicemanager import ServiceManager

service_manager = ServiceManager()

def Service(name):
    return service_manager.activate_service(name)
