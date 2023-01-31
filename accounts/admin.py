from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "uuid", ]


class AdminProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
    
class ProfileUserAdmin(UserAdmin):
    inlines = (AdminProfileInline)
    
    
admin.site.register(AdminUserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
