from django.db import models

class CalendarEvent(models.Model):
    MONTH_CHOICES = [
        ("January", "January"), ("February", "February"), ("March", "March"),
        ("April", "April"), ("May", "May"), ("June", "June"),
        ("July", "July"), ("August", "August"), ("September", "September"),
        ("October", "October"), ("November", "November"), ("December", "December"),
    ]

    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    day = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=100, blank=True, null=True)     
    location = models.CharField(max_length=255, blank=True, null=True) 
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("month", "day")

    def __str__(self):
        return f"{self.month} {self.day} - {self.title}"
