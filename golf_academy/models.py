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