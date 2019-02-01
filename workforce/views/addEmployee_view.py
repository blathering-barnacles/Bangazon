from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Employee, Department

def addEmployee(request):
    '''
    [Method is used to take information sent from the template and post a new employee to the employee table.]
    TICKET 2: R Lancaster

    Arguments:
        request

    Returns:
        [redirect] -- successful completion of object saving to table will redirect the user to the list of employees.
    '''
    if request.method == 'GET':
        # get the departments so that names can display in the dropdown menu
        department_list = Department.objects.all()
        context = {"department_list" : department_list}
        #render the form page
        return render(request, 'workforce/addEmployee.html', context)
    elif request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        startDate = request.POST['startDate']
        isSupervisor = request.POST['isSupervisor']
        department = request.POST['department']
        departmentName = Department.objects.get(id=department)
        obj = Employee(firstName=firstName.title(), lastName=lastName.title(), startDate=startDate, isSupervisor=isSupervisor, department=departmentName)
        obj.save()
        return HttpResponseRedirect(reverse('workforce:employeeList'))
