from django.contrib import admin
from .models import Category,GalleryPicture,Video,MostViewdVideos

admin.site.register(Category)
admin.site.register(GalleryPicture)
admin.site.register(Video)
admin.site.register(MostViewdVideos)
