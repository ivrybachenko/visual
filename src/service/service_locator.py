class ServiceLocator():
    _services = {}

    def register_service(self, name, service):
        self._services[name] = service

    def get_service(self, name):
        return self._services[name]
