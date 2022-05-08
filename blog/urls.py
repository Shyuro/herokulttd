from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import post
from .import views

urlpatterns = [
    path('', views.slide, name='slide'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('posts/<int:post_id>', post)
]