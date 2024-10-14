from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('login/', login, name='login'), 
    path('signup/', signup, name='signup'), 
    path('list/', list_view, name='list'),
    path('AP/', AP, name='AP'),
    path('P1/', P1, name='P1'),
    path('P2/', P2, name='P2'),
    path('P3/', P3, name='P3'),
    path('P4/', P4, name='P4'),
    path('P5/', P5, name='P5'),
    path('addUser/', addUser, name='add_user'),
    path('loginForm/', loginForm, name='loginForm'),
    path('logout/', logout, name='logout'),
]