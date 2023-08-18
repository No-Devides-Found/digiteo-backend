from .base import *

DEBUG = False  # 로컬에서 True 프로덕션에선 False
ALLOWED_HOSTS = ['43.202.94.215', 'api.digiteo.co.kr']

CORS_ORIGIN_WHITELIST = ['https://digiteo.co.kr', 'https://www.digiteo.co.kr']
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'https://api.digiteo.co.kr/', 'https://api.digiteo.co.kr/']

# 프로덕션만
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
