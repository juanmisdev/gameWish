from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib.auth.models import User
# Register your models here.

# Unregister group to remove it from the admin page:
admin.site.unregister(Group)

# Mix profile into user info:
class ProfileInline(admin.StackedInline):
    model = Profile

# Define a new User admin
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ('username', 'email', 'password')
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)