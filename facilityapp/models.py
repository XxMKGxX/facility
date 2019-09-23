from django.db import models
from django.urls import reverse

# Create your models here.

class Facility(models.Model):
    facility_name = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    description = models.TextField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    floor_area = models.IntegerField()
    site_area = models.IntegerField()
    primary_purpose = models.CharField(max_length=32, choices=[
        ('warehouse','Warehouse'),
        ('production facility','Production Facility'),
        ('offices','Offices'),
    ])

    def get_absolute_url(self):
        return reverse("facilityapp:facility-detail", kwargs={"pk": self.pk})