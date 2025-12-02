from django.db import models

class NewsHeader(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
  

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']








class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publish_date = models.DateField()
    content = models.TextField()
    featured_image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']