from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Count
from ..models import Department

# def departmentList(request):
#     latest_dept_list = Department.objects.all()
#     employee_count_list = Department.objects.annotate(employeeCount=Count('employee'))
#     context = {'latest_dept_list': latest_dept_list, 'employee_count_list': employee_count_list}
#     return render(request, 'workforce/departmentList.html', context)

def departmentList(request):
    latest_dept_list = Department.objects.all().annotate(employeeCount=Count('employee'))
    context = {'latest_dept_list': latest_dept_list}
    return render(request, 'workforce/departmentList.html', context)

