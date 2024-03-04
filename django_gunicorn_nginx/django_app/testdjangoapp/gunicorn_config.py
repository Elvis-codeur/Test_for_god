import os 
command = "/usr/local/bin/gunicorn" 
pythonpath = "/usr/local/bin/python"
bind = "0.0.0.0:{}".format(os.getenv('port_number'))
workers = 3
