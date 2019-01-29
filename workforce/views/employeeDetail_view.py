from django.shortcuts import render, get_object_or_404
from workforce.models import Employee, EmployeeTrainingProgram


def employeeDetail(request, employee_id):
    '''[summary]
    
    Arguments:
        request {[type]} -- [description]
        employee_id {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    employee = get_object_or_404(Employee, pk=employee_id)
    training_programs = EmployeeTrainingProgram.objects.filter(employeeId=employee_id)
    context = { 'employee': employee, 'training_programs': training_programs }
    return render(request, 'workforce/employeeDetail_template.html', context)