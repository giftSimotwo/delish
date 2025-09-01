from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=60)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
