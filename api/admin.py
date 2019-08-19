from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','emp_id','emp_name','emp_salary']

admin.site.register(Employee,EmployeeAdmin)
