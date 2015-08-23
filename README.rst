pywebdata
---------

All the web's data. One API.

Usage

1) Add a file called *my_new_service.py* to the *pywebdata/services/* directory

.. code-block:: python
    
    from pywebdata.baseservice import BaseService
        
    class GoogleElevationAPI(BaseService):
    
        name = 'google-elevation-api'
        
        def __init__(self):
            self.add_url('http://maps.googleapis.com/maps/api/elevation/json?locations=$latitude,$longitude')
            self.add_input('latitude', iotype='float', required=True, min=-90., max=90., incr=1.)
            self.add_input('longitude', iotype='float', required=True, min=-180., max=180., incr=1.)
            self.add_output('elevation', iotype='float')
            self.add_parser(staticmethod(lambda x:x['results']))

2) Run the sample script to use the web service

.. code-block:: python

    from pywebdata import Service
    
    my_new_service = Service('google-elevation-api')
    my_new_service.query(latitude=50, longitude=45)

3) An alternative to adding new services to the *services/* directory is to create a new directory and register it this way:

.. code-block:: python

  from pywebdata import ServiceManager
  ServiceManager.register_path('path/to/new/service/')
