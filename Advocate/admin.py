from django.contrib import admin
from .models import position, Client, user_profile

# Register your models here.
admin.site.register(position)
admin.site.register(Client)
admin.site.register(user_profile)
