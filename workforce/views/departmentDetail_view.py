from django.shortcuts import render, get_object_or_404

from ..models import Department, Employee, TrainingProgram

def index(request):

    '''
    Summary:
        This function gathers all of the objects in the TrainingProgram class, and sticks them in the context.
        It also gathers all of the objects from the Employee class and sticks them in the context.

    Arguments:
        request: The render() shortcut renders templates with a request context. Template context processors take the request object and return a dictionary which is added to the context.

    Returns:
        [type] -- [description]
    '''

    programs_list = TrainingProgram.objects.all()
    employee_list = Employee.objects.all()
    context = { 'programs_list': programs_list, 'employee_list': employee_list }
    return render(request, 'workforce/index.html', context)

def detail(request, department_id):

    departments = get_object_or_404(Department, pk=department_id)
    employee_list = Employee.objects.filter(department_id=department_id)
    context = {'departments': departments, 'employee_list': employee_list}
    return render(request, 'workforce/departmentDetail.html', context)
