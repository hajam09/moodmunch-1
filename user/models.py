from django.contrib.auth.models import User
# User is going to be initialised with [full_name, location, password, email, DoB]
from django.db import models

class CustomerAccount(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    


class RestaurantAccount(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)

