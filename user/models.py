from django.contrib.auth.models import User
# User is going to be initialised with [full_name, location, password, email, DoB]
from django.db import models
#from user_profile.models import CustomerProfile

class User(models.Model):
	accountID = models.AutoField(primary_key=True)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	firstname = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	dateOfBirth = models.DateTimeField()

class CustomerAccount(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('user_profile.CustomerProfile', on_delete=models.CASCADE, default=None)

class RestaurantAccount(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)

