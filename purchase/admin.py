from django.contrib import admin
from purchase import models

# Register your models here.

admin.site.register(models.Card)
admin.site.register(models.Purchase)
