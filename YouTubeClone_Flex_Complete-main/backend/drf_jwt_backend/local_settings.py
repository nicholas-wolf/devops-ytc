# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-($i4oais^rlzvt*k8_u3((8!qyq3=dyka08ts#+@^)+chake%n'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        'USER': 'root',
        'PASSWORD': 'example',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}