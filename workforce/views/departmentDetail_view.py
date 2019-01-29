from django.shortcuts import render, get_object_or_404

from ..models import Department, Employee

def index(request):
    # print("request", request)
    department_list = Department.objects.all()
     # print("from_db", cohort_list)
    context = { 'department_list': department_list }
    # print(context)

    return render(request, 'workforce/index.html', context)

def detail(request, department_id):
    department = get_object_or_404(Department, pk=departmentId_Id)
    employee_list = Employee.objects.filter(department_id=departmentId_Id)
    context = {'department': department, 'employee_list': employee_list}
    return render(request, 'workforce/detail.html', context)