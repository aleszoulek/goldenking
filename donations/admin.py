from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.CharityFund)
admin.site.register(models.Donation)
