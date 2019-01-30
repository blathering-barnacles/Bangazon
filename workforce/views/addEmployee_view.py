from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Employee

def addEmployee(request):
    if request.method != 'POST':
        return render(request, 'workforce/addEmployee.html')
    else:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        startDate = request.POST['startDate']
        supervisor = request.POST['supervisor']
        department = request.POST['department']
        obj = addEmployee(firstname=firstName.title(), lastName=lastName.title(), startDate=startDate, supervisor=supervisor, department=department)
        obj.save()
        return HttpResponseRedirect(reverse('workforce:employeeList'))
