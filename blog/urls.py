from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('trend/', views.trend, name='trending'),
    path('user_name/', views.user_name, name='User_Name'),
    path('hastags/', views.hastags, name='Hastags'),
    path('mp3_data/', views.mp3_data, name='Mp3_Data'),
    path('user_video/', views.user_video, name='User_Video'),
    path('download_video', views.download_video, name='Download'),
    path('all_data/', views.all_data, name='All_Data'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

