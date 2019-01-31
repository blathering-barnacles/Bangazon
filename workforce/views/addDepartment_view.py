from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import Department, Employee, TrainingProgram

def departmentForm(request):
    return render(request, 'workforce/addDepartment.html')

def addDepartment(request):

    department_name = request.POST["department_name"]
    department_budget = request.POST["department_budget"]

    new_department = Department.objects.create(
        name = department_name,
        budget = department_budget
    )

    return HttpResponseRedirect(reverse('workforce:departmentList'))
