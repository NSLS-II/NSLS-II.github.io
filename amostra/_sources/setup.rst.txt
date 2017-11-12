Setup
=======

Installation
-------------

.. warning:: 
   
   The installation instructions are for development setup. We are currently working on deployment instructions for production ready service.


1. Install MongoDB
************************
If you are in a beamline environment, MongoDB is already instaled and ready to use. However, if you are testing this on a local machine or on a cloud environment, refer to the MongoDB documentation: https://docs.mongodb.org/manual/installation/

We are running v 3.2 for our development and new deployment setup.

2. Required Packages for the Server
******************************************************
You can use a sandbox approach and deploy the server on a separate environment if you want full separation and mobility of this server. Alternatively, you could use the system Python libraries. The shortfall of this approach is, system Python environments usually fall behind in terms of version. This service is intended to run on Python 3.5.

The required packages for the server side are: tornado, jsonschema, pyyaml, ujson, pytz, pymongo.


3. Server Startup
********************

Once the environment installation is complete, the server can be started via command line, using: 

.. code-block:: python
   
   python startup.py --mongo_port <mongo-daemon-port> --mongo_host <mongo-daemon-host> --database amostra --service-port 7770 --log_file_prefix <full-path-to-logfile>

Once successful, the service will prompt:

.. code-block:: bash

   (dev)➜  amostra git:(master) ✗ python startup.py --mongo_port 27017 --mongo_host localhost --database amostra --log_file_prefix /tmp/amostra.log --service-port 7770
   Starting Amostra service with configuration  {'mongo_port': 27017, 'database': 'amostra', 'mongo_host': 'localhost'}


4. Client Installation
***********************

In order to install and run the client, there are a series of packages needs to be installed: requests, pytz, ujson, pyyaml

In addition to the packages above, the client requires doct.Document: https://github.com/NSLS-II/doct

Once the packages above are installed, one can install the client simply:

.. code-block:: python
   
   python setup.py install


5. Simple Test
********************

Once everthing is good and setup is complete, you can try to create a sample document of your choice by:

.. code-block:: python

   s_ref = SampleReference()
   m_uid = s_ref.create(name='test')
   print(s_ref.find(uid=m_uid))



