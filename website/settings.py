# File: settings.py (Update)

import os
from decouple import config # Zaroori: python-decouple install karna hoga

# --- Security Settings ---

# DEBUG ko environment variable se lein. Production mein False hona chahiye.
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed Hosts: Render ki URL yahaan aayegi.
# Production mein Render ki URL aur domain name daalein.
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1').split(',') 

# SECRET_KEY ko environment variable se lein. Kabhi bhi code mein hardcode na karein!
SECRET_KEY = config('SECRET_KEY')

# --- Database Setup (Render par PostgreSQL best hai) ---
# Yeh code Render ke default database setup ko automatically use karega.
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Static Files (CSS/JS) Setup for Production (WhiteNoise ya Render's service use karein)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'