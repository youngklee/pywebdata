from servicemanager import ServiceManager

def Service(name):
    if not ServiceManager.is_initialized:
        ServiceManager.load_all()
    return ServiceManager.fetch_service(name)
