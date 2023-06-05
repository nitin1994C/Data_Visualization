from django.db import models

# Create your models here.

class Co2Trend(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)