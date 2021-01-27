from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentPagesView, DocumentView


api_router = DefaultRouter()
api_router.register(r'document-pages',DocumentPagesView)
api_router.register(r'documents',DocumentView)

urlpatterns = [
    path('',include(api_router.urls),name="api"),
]
