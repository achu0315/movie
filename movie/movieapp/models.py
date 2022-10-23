from django.db import models


# Create your models here.
class film(models.Model):
    name = models.CharField(max_length=100)
    dec = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
