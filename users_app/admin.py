from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin
from .models import UserProfile



class UserAdmin(BaseUserAdmin):
  fieldsets = (
      (None, {'fields': ('username','email', 'password',)}),
      #(_('Student Information'), {'fields': ('user.cafe_status',)}),
      (_('Personal info'), {'fields': ('first_name', 'last_name',
      									'sex','date_of_birth','region','profile_picture',)}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('phone','user')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone"]
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )

admin.site.register(UserProfile, UserAdmin)