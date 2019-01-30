from django.shortcuts import render, get_object_or_404

from ..models import Department, Employee, TrainingProgram

def index(request):
    department_list = Department.objects.all()
    programs_list = TrainingProgram.objects.all()
    employee_list = Employee.objects.all()
    context = { 'department_list': department_list, 'programs_list': programs_list, 'employee_list': employee_list }
    return render(request, 'workforce/index.html', context)

def detail(request, department_id):
    departments = get_object_or_404(Department, pk=department_id)
    # all_employees = Employee.objects.all()
    employee_list = Employee.objects.filter(department_id=department_id)
    context = {'departments': departments, 'employee_list': employee_list}
    return render(request, 'workforce/departmentDetail.html', context)
