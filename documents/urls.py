from django.urls import path
from django.urls.conf import include,
from rest_framework.routers import DefaultRouter


api_router = DefaultRouter()
api_router.register(r'/documents')

urlpatterns = [
    path('',include(api_router) ),
]
