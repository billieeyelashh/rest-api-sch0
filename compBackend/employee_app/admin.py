from django.contrib import admin

from . import *

admin.site.register(models.Employees)
admin.site.register(models.Salaries)
''' admin.site.register(models.Departments)
admin.site.register(models.DeptEmp)
admin.site.register(models.DeptManager)
admin.site.register(models.Titles) '''
