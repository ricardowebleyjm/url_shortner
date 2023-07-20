from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import URL, Click
from .serializers import URLSerializer, URLSerializerResponse

class URLShortenAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        urls = URL.objects.all().order_by("-created_at")
        serializer = URLSerializerResponse(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        serializer = URLSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            url = serializer.save()
            res = URLSerializerResponse(url)
            return Response(res.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLRedirectAPIView(APIView):
    def post(self, request):
        try:
            shortened_url = request.data.get("shortened_url")
            url = URL.objects.get(shortened_url=shortened_url)
            url.click_count += 1
            url.save()
            click = Click(url=url, ip_address=request.META['REMOTE_ADDR'])
            click.save()
            return Response({'original_url': url.original_url}, status=status.HTTP_200_OK)
        except URL.DoesNotExist:
            return Response({'detail': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

def redirect_path(request, shortened_url:str):
        from django.shortcuts import redirect
        url = URL.objects.get(shortened_url=shortened_url)
        url.click_count += 1
        url.save()
        click = Click(url=url, ip_address=request.META['REMOTE_ADDR'])
        click.save()
        original_url = url.original_url
        response = redirect(original_url)
        return response