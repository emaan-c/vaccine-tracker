from django.db import models
from model_utils import Choices

GENDER = Choices(
	("Male", "Male"),
	("Female", "Female"),
)

LOCATION = Choices(
    ("Toronto", "Toronto"),
    ("Hamilton", "Hamilton"),
    ("Mississauga", "Mississauga"),
    ("Brampton", "Brampton"),
    ("Ottawa", "Ottawa"),
)

class Information(models.Model):
    name = models.CharField(max_length=64)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=16, choices=GENDER, default="Male")
    location = models.CharField(max_length=16, choices=LOCATION, default="Toronto")
    street =  models.CharField(max_length=64)
    postalcode = models.CharField(max_length=6)
    
    def __str__(self):
        return self.name + "'s Information"

class Toronto(models.Model):
    pharmacy = models.CharField(max_length=1000, blank = True)
    address = models.CharField(max_length=1000, blank = True)
    city = models.CharField(max_length=1000, blank = True)
    province = models.CharField(max_length=1000, blank = True)
    mapaddress = models.CharField(max_length=1000, blank = True)
    postal_code = models.CharField(max_length=1000, blank = True)
    vaccine1 = models.CharField(max_length=1000, blank = True)
    vaccine2 = models.CharField(max_length=1000, blank = True)
    appointment_details = models.CharField(max_length=1000, blank = True)
    hours1 = models.CharField(max_length=1000, blank = True)
    hours2 = models.CharField(max_length=1000, blank = True)
    hours3 = models.CharField(max_length=1000, blank = True)
    phone = models.CharField(max_length=1000, blank = True)
    website = models.CharField(max_length=1000, blank = True)
    longitude = models.CharField(max_length=1000, blank = True)
    latitude = models.CharField(max_length=1000, blank = True)
    distance_from_user = models.CharField(max_length=1000, blank = True)

    def __str__(self):
        return self.pharmacy

class Hamilton(models.Model):
    pharmacy = models.CharField(max_length=1000, blank = True)
    address = models.CharField(max_length=1000, blank = True)
    city = models.CharField(max_length=1000, blank = True)
    province = models.CharField(max_length=1000, blank = True)
    mapaddress = models.CharField(max_length=1000, blank = True)
    postal_code = models.CharField(max_length=1000, blank = True)
    vaccine1 = models.CharField(max_length=1000, blank = True)
    vaccine2 = models.CharField(max_length=1000, blank = True)
    appointment_details = models.CharField(max_length=1000, blank = True)
    hours1 = models.CharField(max_length=1000, blank = True)
    hours2 = models.CharField(max_length=1000, blank = True)
    hours3 = models.CharField(max_length=1000, blank = True)
    phone = models.CharField(max_length=1000, blank = True)
    website = models.CharField(max_length=1000, blank = True)
    longitude = models.CharField(max_length=1000, blank = True)
    latitude = models.CharField(max_length=1000, blank = True)
    distance_from_user = models.CharField(max_length=1000, blank = True)

    def __str__(self):
        return self.pharmacy

class Mississauga(models.Model):
    pharmacy = models.CharField(max_length=1000, blank = True)
    address = models.CharField(max_length=1000, blank = True)
    city = models.CharField(max_length=1000, blank = True)
    province = models.CharField(max_length=1000, blank = True)
    mapaddress = models.CharField(max_length=1000, blank = True)
    postal_code = models.CharField(max_length=1000, blank = True)
    vaccine1 = models.CharField(max_length=1000, blank = True)
    vaccine2 = models.CharField(max_length=1000, blank = True)
    appointment_details = models.CharField(max_length=1000, blank = True)
    hours1 = models.CharField(max_length=1000, blank = True)
    hours2 = models.CharField(max_length=1000, blank = True)
    hours3 = models.CharField(max_length=1000, blank = True)
    phone = models.CharField(max_length=1000, blank = True)
    website = models.CharField(max_length=1000, blank = True)
    longitude = models.CharField(max_length=1000, blank = True)
    latitude = models.CharField(max_length=1000, blank = True)
    distance_from_user = models.CharField(max_length=1000, blank = True)

    def __str__(self):
        return self.pharmacy

class Brampton(models.Model):
    pharmacy = models.CharField(max_length=1000, blank = True)
    address = models.CharField(max_length=1000, blank = True)
    city = models.CharField(max_length=1000, blank = True)
    province = models.CharField(max_length=1000, blank = True)
    mapaddress = models.CharField(max_length=1000, blank = True)
    postal_code = models.CharField(max_length=1000, blank = True)
    vaccine1 = models.CharField(max_length=1000, blank = True)
    vaccine2 = models.CharField(max_length=1000, blank = True)
    appointment_details = models.CharField(max_length=1000, blank = True)
    hours1 = models.CharField(max_length=1000, blank = True)
    hours2 = models.CharField(max_length=1000, blank = True)
    hours3 = models.CharField(max_length=1000, blank = True)
    phone = models.CharField(max_length=1000, blank = True)
    website = models.CharField(max_length=1000, blank = True)
    longitude = models.CharField(max_length=1000, blank = True)
    latitude = models.CharField(max_length=1000, blank = True)
    distance_from_user = models.CharField(max_length=1000, blank = True)

    def __str__(self):
        return self.pharmacy

class Ottawa(models.Model):
    pharmacy = models.CharField(max_length=1000, blank = True)
    address = models.CharField(max_length=1000, blank = True)
    city = models.CharField(max_length=1000, blank = True)
    province = models.CharField(max_length=1000, blank = True)
    mapaddress = models.CharField(max_length=1000, blank = True)
    postal_code = models.CharField(max_length=1000, blank = True)
    vaccine1 = models.CharField(max_length=1000, blank = True)
    vaccine2 = models.CharField(max_length=1000, blank = True)
    appointment_details = models.CharField(max_length=1000, blank = True)
    hours1 = models.CharField(max_length=1000, blank = True)
    hours2 = models.CharField(max_length=1000, blank = True)
    hours3 = models.CharField(max_length=1000, blank = True)
    phone = models.CharField(max_length=1000, blank = True)
    website = models.CharField(max_length=1000, blank = True)
    longitude = models.CharField(max_length=1000, blank = True)
    latitude = models.CharField(max_length=1000, blank = True)
    distance_from_user = models.CharField(max_length=1000, blank = True)


    def __str__(self):
        return self.pharmacy