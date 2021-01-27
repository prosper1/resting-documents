from typing import Text
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Document, TextPages



class DocumentPagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TextPages
        fields = (
            'document',
            'page_number',
            'content',
        )


class DocumentSerializer(serializers.ModelSerializer):
    pages = StringRelatedField(many=True)

    class Meta:
        model = Document
        fields = (
            'id',
            'title',
            'file',
            'has_page',
            'pages',
        )