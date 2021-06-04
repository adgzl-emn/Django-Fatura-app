from django.db import models
from datetime import datetime,date
# Create your models here.
class Faturalar(models.Model):
    baslik = models.CharField(max_length=100)
    fiyat = models.IntegerField(blank=True)
    odendi = models.BooleanField(default=False)
    tarih = models.DateField(blank=True )
    kullanici = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
    


