from django.db import models


class ShortURL(models.Model):
    long_url = models.URLField()
    shortcode = models.CharField(max_length=5, unique=True)
