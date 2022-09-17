from django.contrib import admin
from django.apps import apps

admin.site.register(apps.all_models['app_4'].values())

# Register your models here.
