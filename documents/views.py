from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Document,TextPages
from .serializers import DocumentSerializer
from rest_framework import viewsets
from rest_framework.authentication import (
    BaseAuthentication,
    TokenAuthentication,
    SessionAuthentication
)
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .paginations import CustomPagination

# Create your views here.

class DocumentPagesView(viewsets.ModelViewSet):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication
    ]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    queryset = TextPages.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('document',)
    search_fields = ['document']
    http_method_names = ['get']

    
    

    
 
