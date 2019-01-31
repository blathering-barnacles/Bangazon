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


    all_employees = Employee.objects.all()
    context = { 'all_employees' : all_employees }
    return render(request, 'workforce/employeeList.html', context)