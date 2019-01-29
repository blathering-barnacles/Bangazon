from django.shortcuts import render
from ..models import Department, Employee

def index(request):
    department_list = Department.objects.all()
    context = { 'department_list': department_list }
    return render(request, 'workforce/index.html', context)

def detail(request, departmentId_id):
    departments = get_object_or_404(Department, pk=department_id)
    employee_list = Employee.objects.filter(departmentId_id=department_id)
    context = { 'departments': departments, 'employee_list': employee_list }
    return render(request, 'workforce/departmentDetail.html', context)
# Create your views here.
