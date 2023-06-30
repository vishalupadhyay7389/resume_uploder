from django.contrib import admin
from .models import Profile 

# Register your models here.
@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' , 'dob' , 'state' , 'gender' , 'location' , 'pImage' , 'rdoc']
