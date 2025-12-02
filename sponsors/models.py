from django.db import models

# Create your models here.
class SponsorHeader(models.Model):
    title = models.CharField(max_length=200, default="Our Sponsors")
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    background_image = models.ImageField(upload_to='sponsors/', blank=True, null=True)

    class Meta:
        verbose_name = "Sponsor Header"
        verbose_name_plural = "Sponsor Header"

    def __str__(self):
        return self.title






class PartnershipSection(models.Model):
    small_title = models.CharField(max_length=255, default="Together We Grow the Game")
    main_title = models.CharField(max_length=255, default="Building Partnerships")
    description = models.TextField()
    image = models.ImageField(upload_to='partners/', blank=True, null=True)

    class Meta:
        verbose_name = "Partnership Section"
        verbose_name_plural = "Partnership Section"

    def __str__(self):
        return self.main_title






class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/')
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    partner_id = models.SlugField(unique=True)  

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name




class PartnershipApplication(models.Model):
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    cr_number = models.CharField("CR No (Registration Number)", max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    additional_notes = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.company_name}"