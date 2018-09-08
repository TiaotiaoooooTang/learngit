"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#　获取当前Ｄｊａｎｇｏ项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    # __file__为当前文件的路径


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '83(77y=$spoto^s0n1sl-9n9p6rm2z-ce%93@knkf3fy+)(^fk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    # 开启调试模式

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'request_vs_response.apps.RequestVsResponseConfig',
    'booktest.apps.BooktestConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'sy06_django'  # 数据库名字
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'   # 使用中文



# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'   # 使用中国时间

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 制定访问静态文件url地址的前缀
STATIC_URL = '/static/'
# 设置djangp中静态文件的保存目录
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_files')]


# django框架的缓存设置（默认是服务器内存）redis 存储速度高，且支持数据持久化
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 指定使用的redis的地址
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
     # 可以自己开辟redis存储空间
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 指定使用的redis的地址
        "LOCATION": "redis://127.0.0.1:6379/2",   # 2号库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 设置将session信息存储到缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指定session存储到缓存中的哪个空间
SESSION_CACHE_ALIAS = "default"

MEDTA_ROOT = os.path.join(BASE_DIR,'static_files/media')


