import uuid
from .models import ShortURL


def generate_shortcode() -> str:
    while True:
        code = str(uuid.uuid4())[:5]
        if not ShortURL.objects.filter(shortcode=code).exists():
            return code
