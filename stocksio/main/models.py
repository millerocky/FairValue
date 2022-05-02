from django.db import models

class Stocksy(models.Model):
    picture = models.ImageField(upload_to='images')
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)


    def __str__(self):
        return self.name