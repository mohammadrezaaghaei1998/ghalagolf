from django.shortcuts import render
from .models import GalleryItem, Category, GalleryPicture,Video,MostViewdVideos

def gallery(request):
    item = GalleryItem.objects.first()
    categories = Category.objects.all()
    pictures = GalleryPicture.objects.all()
    videos = Video.objects.all()

    left_video = MostViewdVideos.objects.filter(position="left").first()
    right_videos = MostViewdVideos.objects.filter(position="right").order_by("order")

    return render(request, 'gallery.html', {
        'item': item,
        'categories': categories,
        'pictures': pictures,
        'videos': videos,
        'left_video': left_video,
        'right_videos': right_videos,
    })