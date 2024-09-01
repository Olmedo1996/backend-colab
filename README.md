# BACKEND COLAB TRACKING

## Base folder structure
```
backend-colab/
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── api/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   └── v2/
│       ├── __init__.py
│       ├── projects/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── serializers.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   └── tests.py
│       └── urls.py
├── core/
│   ├── __init__.py
│   ├── models.py
│   └── utils.py
├── manage.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── .env
├── .gitignore
├── CHANGELOG.py
└── README.md
```