from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.user)
admin.site.register(models.room)
admin.site.register(models.meeting)
