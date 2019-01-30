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
    '''
    Summary:
        This function gathers all of the objects in the Department class instance and performs an annotate as well as Count method in order to gather the departmentId's from the Employee objects and match them to the id's in the department table. This is how we get the count of employees in each department. This method also of course provides us with all of the data in the Department table

    Arguments:
        request: The render() shortcut renders templates with a request context. Template context processors take the request object and return a dictionary which is added to the context.

    Returns:
        [type] -- [description]
    '''

    latest_dept_list = Department.objects.all().annotate(employeeCount=Count('employee'))
    context = {'latest_dept_list': latest_dept_list}
    return render(request, 'workforce/departmentList.html', context)

