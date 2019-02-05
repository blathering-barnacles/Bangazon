from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Employee, Department

def employeeList(request):
    """[Method gets a list of all objects in the Employee table]
        Ticket 1: R Lancaster

    Arguments:
        request

    Returns:
        Returns the information over to the employeeList template.
    """
    employees_sql = ' SELECT * FROM workforce_employee '

    all_employees = Employee.objects.raw(employees_sql)
    context = { 'all_employees' : all_employees }
    return render(request, 'workforce/employeeList.html', context)