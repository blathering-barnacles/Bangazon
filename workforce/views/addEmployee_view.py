from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Employee, Department

def addEmployee(request):
    if request.method != 'POST':
        return render(request, 'workforce/addEmployee.html')
    else:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        startDate = request.POST['startDate']
        supervisor = request.POST['supervisor']
        print(supervisor)
        department = request.POST['department']
        taco = Department.objects.get(id=department)
        obj = Employee(firstName=firstName.title(), lastName=lastName.title(), startDate=startDate, isSupervisor=supervisor, department=taco)
        obj.save()
        return HttpResponseRedirect(reverse('workforce:employeeList'))
