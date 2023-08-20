from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=05*2^0i7_5$gbt8ql6yodp*(1=wb^0h=d34w4k3pw6a#%!4^!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / "media"
