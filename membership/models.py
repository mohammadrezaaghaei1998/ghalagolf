from django.db import models
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.
class MembershipHeader(models.Model):
    title = models.CharField(max_length=200, default="Get Out & Play")
    subtitle = models.TextField(default="Explore membership benefits, fees, and all the amenities awaiting you")
    image = models.ImageField(upload_to='membership/', blank=True, null=True) 

    def __str__(self):
        return self.title





class AmenitiesSection(models.Model):
    description = models.TextField(
        default="Whether playing our 18-hole championship course or our 9-hole course, we have plenty of options when it comes to green fees with weekend and weekday as well as summer and winter rates available."
    )

    def __str__(self):
        return self.description




class AmenityCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    category = models.ForeignKey(AmenityCategory, on_delete=models.CASCADE, related_name='amenities', null=True, blank=True)

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='amenities/', blank=True, null=True)

    def __str__(self):
        return self.name







class GolfFee(models.Model):
    description = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)

    def __str__(self):
        return self.description
