from django.contrib import admin

# Register your models here.
from app.models import Cars, Details

admin.site.register(Cars)
admin.site.register(Details)