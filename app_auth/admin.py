from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class CustomGroupAdmin(GroupAdmin, ModelAdmin):
    pass