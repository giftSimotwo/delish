from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def delivery_fee(self):
        if self.price < 100:
            return 30
        elif self.price >= 100 and  self.price <= 700:
            return 60
        else:
            return 100

    def __str__(self):
        return self.name
    
