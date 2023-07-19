from rest_framework import serializers
import random
import string
from shortner.models import URL


class URLSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=255)
    
    def generate_shortened_url(self):
            characters = string.ascii_letters + string.digits
            url = ''.join(random.choice(characters) for _ in range(7))
            scheme = self._context['request']._stream._current_scheme_host + str("/") + url
            return scheme
        
        
    def create(self, validated_data):
        shortened_url = self.generate_shortened_url()
        
        return URL.objects.create(
            original_url=validated_data['url'], 
            shortened_url=shortened_url,
        )

class URLSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ("id", "original_url", "shortened_url", "created_at", "click_count",)