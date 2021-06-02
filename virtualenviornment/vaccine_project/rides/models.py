from django.db import models

class UberInformation(models.Model):
    name = models.CharField(max_length=64)
    street =  models.CharField(max_length=64)
    postalcode = models.CharField(max_length=6)
    city = models.CharField(max_length=6)
    
    def __str__(self):
        return self.name + "'s Information"
