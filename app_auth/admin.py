from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth import get_user_model
from unfold.admin import ModelAdmin

# Récupère votre CustomUser configuré dans AUTH_USER_MODEL
User = get_user_model()

admin.site.unregister(Group)

@admin.register(Group)
class CustomGroupAdmin(GroupAdmin, ModelAdmin):
    pass

@admin.register(User)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    # Permet de voir et modifier le champ 'role' dans l'interface Unfold
    fieldsets = UserAdmin.fieldsets + (
        ("Rôles & Permissions", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff")