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

# Create your views here.

class DocumentPagesView(viewsets.ModelViewSet):
    authentication_classes = [
        BaseAuthentication,
        TokenAuthentication,
        SessionAuthentication
    ]
    queryset = Document.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        """
            Get and permission cart
        """
        try:
            username = self.request.content_params.get('')
            pages = TextPages.objects.filter()

            

            return pages 
