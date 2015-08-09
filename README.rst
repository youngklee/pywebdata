pywebdata
---------

All the web's data. One API.

Usage

1) Add a file called *my_new_service.py* to the *services/* directory

.. code-block:: python

 from pywebdata.baseservice import BaseService
 
 class My_New_Service(BaseService):
 
  name = 'my-service'
  
  def query(self, **kwargs):
    #do stuff

2) Run the sample script to use the web service

.. code-block:: python

    from pywebdata import Service
    
    my_new_service = Service('my-service')
    my_new_service.query(latitude=50, longitude=45)
