from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  dummy = [
    {
      'id': 1,
      'title': 'Django',
      'content': 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.',
      'image': 'https://example.com/django.jpg'
    },
    {
      'id': 2,
      'title': 'Flask',
      'content': 'Flask is a lightweight WSGI web application framework in Python.',
      'image': 'https://example.com/flask.jpg'
    },
    {
      'id': 3,
      'title': 'FastAPI',
      'content': 'FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.',
      'image': 'https://example.com/fastapi.jpg'
    },
    {
      'id': 4,
      'title': 'Pyramid',
      'content': 'Pyramid is a small, fast, down-to-earth, open source Python web framework.',
      'image': 'https://example.com/pyramid.jpg'
    }
  ]

  return render(request, 'intro.html', {'lessons': dummy})