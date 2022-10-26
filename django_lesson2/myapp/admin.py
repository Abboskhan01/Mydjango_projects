from django.contrib import admin
from django.apps import apps
# from .models import Category, Author, Book, Person

admin.site.register(apps.all_models['myapp'].values())