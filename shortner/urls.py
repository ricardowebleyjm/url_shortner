from django.urls import path
from shortner import views


urlpatterns = [
    path('', views.URLShortenAPIView.as_view(), name="shortner"),
    path('clicked/', views.URLRedirectAPIView.as_view(), name='clicked'),
]
