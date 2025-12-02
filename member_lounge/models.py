from django.db import models



class MemberLoungeHeader(models.Model):
    title = models.CharField(max_length=255, default="Feel the Atmosphere")
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    header_image = models.ImageField(upload_to="headers/member_lounge/")

    def __str__(self):
        return self.title





class MemberLoungeDescription(models.Model):
    title = models.CharField(max_length=255, default="Relax by the 18th")
    description_1 = models.TextField(blank=True, null=True)
    description_2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title




class LoungeFeature(models.Model):
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class, e.g. fa-solid fa-utensils")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title





class MemberLoungeGallery(models.Model):
    image = models.ImageField(upload_to='member_lounge/gallery/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self. alt_text or f"Gallery Image {self.id}"





class LoungeBannerInfo(models.Model):
    title = models.CharField(max_length=255, default="Relax at Ghala Golf Club Lounge")
    description = models.TextField(
        default="Experience premium comfort and exceptional amenities at the Ghala Golf Club Lounge, your perfect retreat before a game or event."
    )

    banner_image = models.ImageField(upload_to="member_lounge/location_banners/", blank=True, null=True)
   

    def __str__(self):
        return self.title
