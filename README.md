Memory_middleware
=================
A middleware to check the memory utilized by the url request-response process.
Developed at the GWU Libraries in Washington, DC, USA.

Installation:      
Developed using Python 2.7,Django 1.5 and psutil.  
psutil is a python package used for retrieving information on running processes and the system utilization.

get the psutil packge on VM:       
sudo pip install psutil

Place the memory.py file in the middleware directory of django settings. The exact location is:      
ENV/lib/python2.7/site-packages/django/middleware

Include the middleware file-name in your project settings file under the MIDDLEWARE_CLASSES. It should look like this:
MIDDLEWARE_CLASSES = (    
     ....      
     ...     
     
    'django.middleware.memory.MemoryUsageMiddleware',
)


Cloning:   
If you clone the middleware using the url : https://github.com/gwu-libraries/Memory_middleware.git
You will get a whole new directory at your current location, from there you will have to make the above mentioned changes to get it working.    
If this directory is kept anywhere in your project or outside, it will not impact the already present django settings. 
