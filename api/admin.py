from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User, Driver, Vehicle, Client, Trip, Merchandise, Container, Vidange, Panne, Maintenance, Entretien
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete=False
    verbose_plural_name="User Profile"
    fk_name = 'user'  

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    
    list_display_links = ['email']
    search_fields = ('email',)
    ordering = ('email',)
    inlines = (UserProfileInline,)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name','user_type')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')}
         ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin) 

# Registering the HBZ TMS API models here
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Client)
admin.site.register(Trip)
admin.site.register(Merchandise)
admin.site.register(Container)
admin.site.register(Vidange)
admin.site.register(Panne)
admin.site.register(Maintenance)
admin.site.register(Entretien)