from django.db import models

# Create your models here.


class Sales(models.Model):
    items = models.CharField(max_length=50)
    price = models.FloatField()


    def __str__(self):
        return str(self.items)