from django.contrib import admin

from .models import Restaurant, Menu, Dishes, Review, Reservation
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Dishes)
admin.site.register(Review)
admin.site.register(Reservation)
