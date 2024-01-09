from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', views.simple, name='simple'),
    path('dinamico/<str:name>',views.dinamico, name='dinamico'),
 

    path('estaticos/',views.estaticos,name = 'estaticos'),

    path('herencia/',views.herencia,name='herencia'),
    path('',views.index,name="index"),
]
