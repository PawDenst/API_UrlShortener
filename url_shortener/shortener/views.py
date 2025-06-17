from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import ShortURL
from .serializers import ShortURLSerializer
from .utils import generate_shortcode


def redirect_view(request: HttpRequest, shortcode: str) -> HttpResponse:
    short_url = get_object_or_404(ShortURL, shortcode=shortcode)
    return redirect(short_url.long_url)


class ShortenURLView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ShortURLSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        long_url: str = serializer.validated_data['long_url']
        shortcode: str = generate_shortcode()
        short_url: ShortURL = ShortURL.objects.create(long_url=long_url, shortcode=shortcode)
        return Response({'short_url': request.build_absolute_uri(f'/shrt/{short_url.shortcode}')}, status=201)


class ExpandURL(APIView):
    def get(self, request: Request, shortcode: str) -> Response:
        short_url: ShortURL = get_object_or_404(ShortURL, shortcode=shortcode)
        return Response({'long_url': short_url.long_url})
