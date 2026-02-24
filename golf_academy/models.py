from django.db import models

# Create your models here.


class AcademyApplication(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    membership_type = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)
    handicap = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.membership_type}"




class GolfAcademyContent(models.Model):
    title = models.CharField(max_length=255)
    thumbnail_image = models.ImageField(upload_to='academy_images/')
    video_file = models.FileField(upload_to='academy_videos/')

    def __str__(self):
        return self.title



class GolfAcademyGallery(models.Model):
    image_main = models.ImageField(upload_to='golf_academy/', verbose_name="Main Image", blank=True)
    image = models.ImageField(upload_to='golf_academy/', verbose_name="Image", blank=True)

    def __str__(self):
        return f"Gallery Item #{self.id}"

    def main_image_tag(self):
        if self.image_main:
            return format_html('<img src="{}" width="100" />', self.image_main.url)
        return "No Image"
    main_image_tag.short_description = 'Main Image'




class GolfAcademyGalleryDescription(models.Model):
   
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title




