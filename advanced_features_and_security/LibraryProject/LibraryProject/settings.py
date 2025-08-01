"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cgt@vct6(kv1acc@$!f#&)xyr3%u=$f!o0-*je@)!=kb7g^f0_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Custom User Model Configuration
# Set the custom user model as the default for authentication
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# SECURITY SETTINGS
# =============================================================================

# Security Best Practices Implementation
# These settings enhance application security against common vulnerabilities

# HTTPS and SSL Configuration
# In production, set DEBUG = False and configure these settings appropriately

if not DEBUG:  # Production security settings
    # Force HTTPS redirects for all HTTP requests
    SECURE_SSL_REDIRECT = True
    
    # HTTP Strict Transport Security (HSTS)
    # Instructs browsers to only access the site via HTTPS for the specified time
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Secure Cookie Settings
    # Ensure cookies are only transmitted over HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Additional security headers
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
else:  # Development settings
    # For development, we set less restrictive settings
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    
    # Still apply basic security headers in development
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

# CSRF Protection Settings
# Django's CSRF middleware is already enabled in MIDDLEWARE
# Additional CSRF settings for enhanced security
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript access to CSRF cookie
CSRF_USE_SESSIONS = False    # Use cookie-based CSRF tokens
CSRF_COOKIE_SAMESITE = 'Strict'  # Strict same-site policy for CSRF cookies

# Session Security Settings
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to session cookie
SESSION_COOKIE_SAMESITE = 'Strict'  # Strict same-site policy for session cookies
SESSION_SAVE_EVERY_REQUEST = True   # Refresh session on every request
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expire sessions when browser closes
SESSION_COOKIE_AGE = 3600  # Session timeout: 1 hour

# Security Headers and Content Security Policy
# These headers help prevent XSS, clickjacking, and other attacks
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Proxy SSL Header Configuration
# When using a reverse proxy (like Nginx) that handles SSL termination
# Uncomment the following lines if deploying behind a proxy:
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# This tells Django to trust the X-Forwarded-Proto header from the proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Content Security Policy (CSP) Settings
# Note: For full CSP implementation, consider using django-csp package
# Basic CSP headers can be set in views or middleware

# File Upload Security
# Limit file upload size to prevent DoS attacks
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024   # 5MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 100             # Limit form fields

# Password Security
# Enhanced password validation is already configured above
# Additional password security settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,  # Minimum 8 characters
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Logging Configuration for Security Events
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'security.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Database Security
# For production, use environment variables for database credentials
# Never commit database credentials to version control

# Email Security (if using email functionality)
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# For production, use environment variables for email credentials

# Additional Security Notes:
# 1. Always use HTTPS in production
# 2. Keep Django and all dependencies updated
# 3. Use environment variables for sensitive settings
# 4. Implement proper input validation in forms
# 5. Use Django's ORM to prevent SQL injection
# 6. Implement proper authentication and authorization
# 7. Use CSRF tokens in all forms
# 8. Sanitize user inputs to prevent XSS attacks
# 9. Implement rate limiting for API endpoints
# 10. Regular security audits and penetration testing
