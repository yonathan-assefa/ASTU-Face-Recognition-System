from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(SchoolProgram)
admin.site.register(FieldOfStudy)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentLog)