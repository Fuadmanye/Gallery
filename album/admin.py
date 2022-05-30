from django.contrib import admin
from .models import ImageLocation,ImageCategory,ImagePost

# Register your models here.
admin.site.register(ImageLocation)
admin.site.register(ImageCategory)
admin.site.register(ImagePost)

