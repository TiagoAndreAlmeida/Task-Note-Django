from django.contrib import admin

from .models import UserProfile, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# Register your models here.
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Task)