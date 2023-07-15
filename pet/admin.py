from django.contrib import admin
from .models import Pet
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Pet)
admin.site.unregister(Group)