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

    # employee = get_object_or_404(Employee, pk=employee_id)
    employee_sql = ' SELECT  * from workforce_employee WHERE  workforce_employee.id = %s;'
    employee = Employee.objects.raw(employee_sql, [1])[0]

    training_sql = ' SELECT  * from workforce_employeetrainingprogram WHERE  workforce_employeetrainingprogram.employee_id = %s;'

    training_programs = EmployeeTrainingProgram.objects.raw(training_sql, [employee_id])
    # training_programs = EmployeeTrainingProgram.objects.filter(employee_id=employee_id)
    context = { 'employee': employee, 'training_programs': training_programs }
    # print("CONTEXT", context)
    return render(request, 'workforce/employeeDetail.html', context)