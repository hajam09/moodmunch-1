from django.contrib import admin

# Register your models here.
from .models import User, CustomerAccount, RestaurantAccount

admin.site.register(User)
admin.site.register(CustomerAccount)
admin.site.register(RestaurantAccount)