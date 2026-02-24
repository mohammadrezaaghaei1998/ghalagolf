from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"





class AboutUs(models.Model):
    year = models.CharField(max_length=10)  
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='aboutus_images/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'year']

    def __str__(self):
        return f"{self.year} - {self.title}"





