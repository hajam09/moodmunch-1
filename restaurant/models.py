from django.db import models
from django.contrib.auth.models import User
#from mooduser.models import RestaurantAccount, CustomerAccount

class Restaurant(models.Model):
        userID = models.ForeignKey('user.RestaurantAccount', on_delete=models.CASCADE)
        licenseID = models.CharField(max_length=10)
        rName = models.CharField(max_length=50)
        location = models.CharField(max_length=6)
        phoneNo = models.CharField(max_length=11)


class Menu(models.Model):
        restaunrantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
        lastUpdated = models.DateTimeField()


class Dishes(models.Model):
        menuID = models.ForeignKey(Menu, on_delete=models.CASCADE)
        dishName = models.CharField(max_length=50)
        description = models.CharField(max_length=50)
        allergens = models.CharField(max_length=500)
        price = models.FloatField(default = 0)

class Review(models.Model):
        restaunrantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
        description = models.CharField(max_length=999)
        review_date = models.DateTimeField()
        emoji = models.CharField(max_length=1)

class Reservation(models.Model):
        customerID = models.ForeignKey('user.CustomerAccount', on_delete=models.CASCADE)
        restaunrantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
        numOfSeats = models.IntegerField(default=0)
        date = models.DateTimeField()
