from django.contrib import admin

# Register your models here.
from studentapp import models

admin.site.register(models.Student)
admin.site.register(models.Team)