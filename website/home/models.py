from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300)
    image_1 = models.ImageField(upload_to='', null=True, blank=True, max_length=500)
    image_2 = models.ImageField(upload_to='', null=True, blank=True, max_length=500)
    image_3 = models.ImageField(upload_to='', null=True, blank=True, max_length=500)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name + ' ' + self.category 
