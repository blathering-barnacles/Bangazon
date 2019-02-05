from django.shortcuts import render, get_object_or_404

from ..models import Department, Employee, TrainingProgram

def detail(request, department_id):
    '''
    Method returns department details for a single department

    Arguments:
        request
        department_id

    Returns:
        returns a list of the name and budget of a single Department
    '''

    # departments = get_object_or_404(Department, pk=department_id)
    # employee_list = Employee.objects.filter(department_id=department_id)
    department_sql = 'SELECT * FROM workforce_department WHERE id=%s'
    department = Department.objects.raw(department_sql, [department_id])[0]

    employees_sql = 'SELECT * FROM workforce_employee WHERE department_id=%s'
    employee_list = Employee.objects.raw(employees_sql, [department_id])
    context = {'department': department, 'employee_list': employee_list}
    return render(request, 'workforce/departmentDetail.html', context)
