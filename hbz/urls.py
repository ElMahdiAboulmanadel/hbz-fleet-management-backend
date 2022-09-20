"""
    hbz URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL,document_root=settings.BASE_DIR) + [
    
    path('', admin.site.urls),
]

