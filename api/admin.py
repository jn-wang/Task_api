from django.contrib import admin

# Register your models here.
from api import models

admin.site.register(models.Task)
admin.site.register(models.UserInfo)