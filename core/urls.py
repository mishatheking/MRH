from django.urls import path
from . import views

urlpatterns = [
    # path('base', views.base, name='base'),
    path('home', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('fixers', views.fixers, name='fixers'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]