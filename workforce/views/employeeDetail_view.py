from django.shortcuts import render, get_object_or_404
from workforce.models import Employee, EmployeeTrainingProgram


def employeeDetail(request, employee_id):
    '''[renders the first name, last name, start date, and department name for an individual employee]
    Author: J.Barnett

    Arguments:
        request
        employee_id [the id of the individual employee]

    Returns:
        The rendered employee detail template with the employee matching that employee_id
    '''

    employee = get_object_or_404(Employee, pk=employee_id)
    training_programs = EmployeeTrainingProgram.objects.filter(employee_id=employee_id)
    context = { 'employee': employee, 'training_programs': training_programs }
    return render(request, 'workforce/employeeDetail_template.html', context)