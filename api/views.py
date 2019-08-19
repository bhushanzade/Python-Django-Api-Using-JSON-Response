from django.http import JsonResponse
from api.models import Employee
from django.views.generic import View
# Create your views here.

class GetEmployeeByID(View):
    def get(self,request,id,*args,**kwargs):
        emp = Employee.objects.get(id=id)
        emp_data={
            'emp_id' : emp.emp_id,
            'emp_name' : emp.emp_name,
            'emp_salary' : emp.emp_salary
        }
        return JsonResponse(emp_data)

class getAllEmployee(View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.all().values('emp_id','emp_name','emp_salary')
        empList = list(emp)
        return JsonResponse(empList,safe = False)