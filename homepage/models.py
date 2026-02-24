from django.db import models

# Create your models here.


class HomePageHeader(models.Model):
    title = models.CharField(max_length=255, default="Ghala Golf Club")
    subtitle = models.CharField(max_length=255, default="Since 1971")
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title












class Service(models.Model):
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    button_url = models.URLField(blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)

    @property
    def formatted_order(self):
        return f"{self.order:02d}"  

    def __str__(self):
        return self.title







class AboutUs(models.Model):
  
    image = models.ImageField(upload_to='about_images/')
    description_1 = models.TextField(help_text="First paragraph with highlighted text")
    description_2 = models.TextField(help_text="Second paragraph")
    description_3 = models.TextField(help_text="Third paragraph")
    button_text = models.CharField(max_length=50, default="View More")
    button_url_name = models.CharField(max_length=50, default="about-us", help_text="URL name for the button link")

    def __str__(self):
        return self.description_1







class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True, help_text="Upload a team member's photo")
    description = models.TextField(blank=True, null=True, help_text="Short bio or description for the team member")

    order = models.PositiveIntegerField(default=0, help_text="Ordering of team members on the page")

    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name



class Insight(models.Model):
    quote = models.TextField(help_text="Personal and engaging statement")
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='insight_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Insight"
        verbose_name_plural = "Insights"

    def __str__(self):
        return f"{self.author_name} - {self.author_title or 'No title'}"




class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "Contact Information"