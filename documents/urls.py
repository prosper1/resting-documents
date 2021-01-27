from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentPagesView


api_router = DefaultRouter()
api_router.register(r'documents',DocumentPagesView)

urlpatterns = [
    path('',include(api_router.urls),name="api"),
]
