from django.contrib import admin
from .models import Profile, Cart, CartItams, Coupon

# Register your models here.


admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItams)
admin.site.register(Coupon)