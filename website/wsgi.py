# File: your_project_name/wsgi.py (Standard Django file)

# ... (lines before)
import os

from django.core.wsgi import get_wsgi_application

# Yahaan 'your_project_name' ko 'website' se badlein
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

application = get_wsgi_application()
