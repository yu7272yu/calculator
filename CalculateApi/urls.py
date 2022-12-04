from django.urls import include, re_path as url

from . import views
 
urlpatterns = [
    url('calculate', views.calculate),
    url('test', views.test),
    url('login', views.login),
    url('callback', views.callback),
    url('small', views.login_small),
    url('callback_user', views.callback_user),

]