"""
WSGI config for calculator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculator.settings')

application = get_wsgi_application()

# [uwsgi]
# # django项目监听的socket文件（可以使用端口代替）
# socket = ./calculator.sock
# # django项目所在目录
# chdir = .
# # django项目wsgi文件
# wsgi-file = ./calculator/wsgi.py
 
# master = true
# processes = 2
# threads = 4
# vacuum = true
 
# # 通过touch reload可以重启uwsgi服务器
# touch-reload = ./reload
# # 日志输出
# daemonize = calculator.log