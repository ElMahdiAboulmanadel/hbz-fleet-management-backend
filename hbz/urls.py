"""
    hbz URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = static(settings.MEDIA_URL,document_root=settings.BASE_DIR) + [
    path("api/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', admin.site.urls),
]
