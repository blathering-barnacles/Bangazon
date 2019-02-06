from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..forms import AddDeptForm

from ..models import Department, Employee, TrainingProgram

from django.db import connection


# def departmentForm(request):
#     '''
#     [Renders the add new department form template]
#     '''
#     return render(request, 'workforce/addDepartment.html')

def addDepartment(request):
    '''
    [Posts the data from the add new department form as a new row in the department table]
    '''

    if request.method == 'GET':
        add_dept_form = AddDeptForm()
        return render(request, 'workforce/addDepartment.html', {'form': add_dept_form})

    elif request.method == "POST":

        department_name = request.POST["department_name"]
        department_budget = request.POST["department_budget"]


    with connection.cursor() as cursor:
        cursor.execute('INSERT into workforce_department VALUES(%s, %s, %s)', [None,department_name, department_budget])

        return HttpResponseRedirect(reverse('workforce:departmentList'))

