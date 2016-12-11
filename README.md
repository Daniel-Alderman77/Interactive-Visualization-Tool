<h1>Interactive Visualization Tool</h1>

Author: Daniel Alderman
Date: 11/12/16

**Requirements**
- Python 2.7
- For Python libraries please see requirements.txt
- This software and instructions have been tested on Unix based systems.

**Directory Structure**
<pre>
.
├── Client-side\ (Long\ Timeout)
│   ├── Client.py
│   ├── ExportTestResults.py
│   ├── FaultDetection.py
│   ├── FileHandler.py
│   ├── Prediction.py
│   ├── RESTClient.py
│   ├── Views.py
│   ├── Visualizer.py
│   ├── WebServiceClient.py
│   └── prediction_cache
│       ├── log-1-2016-03-22T15-04-36.1784977Z.xml
│       ├── ...xml
├── Client-side\ (Standard)
│   ├── Client.py
│   ├── ExportTestResults.py
│   ├── FaultDetection.py
│   ├── FileHandler.py
│   ├── Prediction.py
│   ├── RESTClient.py
│   ├── Views.py
│   ├── Visualizer.py
│   ├── WebServiceClient.py
│   └── prediction_cache
│       ├── log-1-2016-03-22T15-04-36.1784977Z.xml
│       ├── ...xml
├── Client-side\ (Without\ Prediction)
│   ├── Client.py
│   ├── ExportTestResults.py
│   ├── FaultDetection.py
│   ├── FileHandler.py
│   ├── RESTClient.py
│   ├── Views.py
│   ├── Visualizer.py
│   └── WebServiceClient.py
├── README.md
├── Server-side\ (Large\ Dataset)
│   ├── RESTServer.py
│   ├── RESTServer.pyc
│   └── static
│       ├── log-1-2016-03-22T14-22-00.0688618Z.xml
│       ├── ...xml
├── Server-side\ (Medium\ Dataset)
│   ├── RESTServer.py
│   └── static
│       ├── log-1-2016-03-22T14-22-00.0688618Z.xml
│       ├── ...xml
├── Server-side\ (Small\ Dataset)
│   ├── RESTServer.py
│   └── static
│       ├── log-1-2016-03-22T14-22-00.0688618Z.xml
│       ├── ...xml
└── requirements.txt
</pre>

**Creating the Virtual Environment**
If virtualenv has not been installed, install it `pip install virtualenv`.

Navigate into the project directory `cd sc12dja-FYP`.

Then create a virtual environment called 'venv' `virtualenv venv`.

Activate the virtual environment `source venv/bin/activate`.

Then install the required dependencies `pip install -r requirements.txt`.

**Server**
Please select the desired size of dataset (Large, Medium or Small) and naivigate to the corresponding server directory.

If the virtual environment is not activated, activate it `source venv/bin/activate`.

Now run the server with the desired IP address (this IP can be local to the host machine) `python RESTServer.py hosturl`.

**Client**
Please select the desired client (Standard, Long Timeout or Without Prediction) and naivigate to the corresponding server directory.

If the virtual environment is not activated, activate it `source venv/bin/activate`.

Now run the client with the desired the servers IP address, client number and run number `python Client.py hosturl client-number run-number`.
