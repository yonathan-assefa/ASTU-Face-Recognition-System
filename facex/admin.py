from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

admin.site.register(SchoolProgram)
admin.site.register(FieldOfStudy)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Student)
