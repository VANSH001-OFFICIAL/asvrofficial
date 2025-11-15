# File: your_project_name/wsgi.py (Standard Django file)

import os
from django.core.wsgi import get_wsgi_application

# Ensure ki aapka project name yahaan sahi ho
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings') 

application = get_wsgi_application()