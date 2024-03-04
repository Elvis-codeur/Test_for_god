import os 
command = "env/lib/python3.10/site-packages/gunicorn" 
pythonpath = "env/bin/python"
bind = "0.0.0.0:8080"
workers = 3