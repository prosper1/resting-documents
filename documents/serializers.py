from rest_framework import serializers
from .models import TextPages



class DocumentSerializer(serializers.ModelSerializer):
    document = serializers.StringRelatedField(read_only=True,many=False)

    class Meta:
        model = TextPages
        fields = (
            'document',
            'page_number',
            'content',
        )