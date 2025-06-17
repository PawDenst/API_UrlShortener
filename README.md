# URL Shortener API

API for shortening URLs created with Django REST Framework.

## Setup

1. Clone the repository.

2. Create a virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

3. Install dependencies and start the server
```bash
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

4. Automated tests can be run using pytest:
```bash
pytest -v
```

### 1. Create a short URL
```bash
curl -s -X POST http://localhost:8000/api/shorten/ -H "Content-Type: application/json" -d "{\"long_url\": \"https://example.compl.long/longer/test/url\"}"
```

**Response:**

```json
{"short_url":"http://localhost:8000/shrt/2afdc"}
```



### 2. Expand a short URL
```bash
curl http://localhost:8000/api/expand/2afdc/
```

**Response:**

```json
{"long_url":"https://example.compl.long/longer/test/url"}
```

### 3. Redirect using short URL
```bash
curl -I http://localhost:8000/shrt/2afdc/
```

**Response:**
```
HTTP/1.1 302 Found  
Location: https://example.compl.long/longer/test/url
```
