from django.urls import path
from .views import ShortenURLView, ExpandURL

urlpatterns = [
    path('shorten/', ShortenURLView.as_view()),
    path('expand/<str:shortcode>/', ExpandURL.as_view()),
]

