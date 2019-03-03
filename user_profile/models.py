from django.db import models
#from moodmunch.user.models import CustomerAccount

# Create your models here.

class CustomerProfile(models.Model):
	foodPreferences = models.CharField(max_length=1000)
	allergens = models.CharField(max_length=1000)