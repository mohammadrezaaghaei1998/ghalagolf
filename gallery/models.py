from django.db import models

# Create your models here.
class GalleryItem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='gallery/videos/', blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Gallery Item"










class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class GalleryPicture(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='pictures')

    class Meta:
        verbose_name = "Gallery Picture"
        verbose_name_plural = "Gallery Pictures"

    def __str__(self):
        return self.title if self.title else "Gallery Picture"







class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='gallery/videos/')
    poster = models.ImageField(upload_to='gallery/posters/', blank=True, null=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.title






class MostViewdVideos(models.Model):
    POSITION_CHOICES = (
        ('left', 'Left (Main Video)'),
        ('right', 'Right Side Videos'),
    )

    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='videos/thumbnails/')
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    order = models.IntegerField(default=0)  # for sorting right videos

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['position', 'order']

    def __str__(self):
        return self.title