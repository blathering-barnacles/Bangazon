from django.shortcuts import render, get_object_or_404
from workforce.models import Employee


def employeeDetail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    context = { 'employee': employee }
    return render(request, 'workforce/employeeDetail_template.html', context)