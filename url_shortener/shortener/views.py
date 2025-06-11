import uuid
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import Serializer


def generate_shortcode():
    while True:
        code = str(uuid.uuid4())[0:5]
        if not ShortURL.objects.filter(shortcode=code).exists():
            return code


def redirect_view(request, shortcode):
    short_url = get_object_or_404(ShortURL, shortcode=shortcode)
    return redirect(short_url.long_url)


class ShortenURLView(APIView):
    def post(self, request):
        serializer = Serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        long_url = serializer.validated_data['long_url']
        shortcode = generate_shortcode()
        short_url = ShortURL.objects.create(long_url=long_url, shortcode=shortcode)
        return Response({'short_url': request.build_absolute_uri(f'/shrt/{short_url.shortcode}')}, status=201)


class ExpandURL(APIView):
    def get(self, request, shortcode):
        short_url = get_object_or_404(ShortURL, shortcode=shortcode)
        return Response({'long_url': short_url.long_url})
