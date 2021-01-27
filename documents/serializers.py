from rest_framework import serializers
from .models import TextPages



class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TextPages
        fields = (
            'document',
            'page_number',
            'content',
        )