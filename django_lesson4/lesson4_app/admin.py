from django.contrib import admin
from django.apps import apps

admin.site.register(apps.all_models['lesson4_app'].values())



