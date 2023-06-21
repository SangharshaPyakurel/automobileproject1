from django.contrib import admin

from automobile.models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email","password")
admin.site.register(Manufacturer)
admin.site.register(Vechicle)