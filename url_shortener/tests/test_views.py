import pytest
from shortener.models import ShortURL


@pytest.mark.django_db
def test_shorten_url(client):
    long_url = "http://example.com/very/long/url"
    response = client.post("/api/shorten/", data={"long_url": long_url})

    assert response.status_code == 201
    assert "short_url" in response.data
    assert response.data["short_url"].startswith("http://")


@pytest.mark.django_db
def test_expand_url(client):
    long_url = "http://example.com/very/long/url"
    shortcode = "x2345"
    ShortURL.objects.create(long_url=long_url, shortcode=shortcode)

    response = client.get(f"/api/expand/{shortcode}/")

    assert response.status_code == 200
    assert response.data["long_url"] == long_url


@pytest.mark.django_db
def test_redirect_view(client):
    long_url = "http://example.com/very/verylong/url"
    shortcode = "x234z"
    ShortURL.objects.create(long_url=long_url, shortcode=shortcode)

    response = client.get(f"/shrt/{shortcode}/", follow=False)

    assert response.status_code == 302
    assert response.url == long_url


@pytest.mark.django_db
def test_shorten_url_invalid_input(client):
    response = client.post("/api/shorten/", data={})
    assert response.status_code == 400


@pytest.mark.django_db
def test_expand_url_not_found(client):
    response = client.get(f"/api/expand/invalid/")
    assert response.status_code == 404
