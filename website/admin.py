from django.contrib import admin

# Register your models here.
from .models import Comments,Images


admin.site.register(Images)
admin.site.register(Comments)