from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from ..models import TrainingProgram, EmployeeTrainingProgram

# def index(request):
#     programs_list = TrainingProgram.objects.all()
#     context = { 'programs_list': programs_list }
#     return render(request, 'workforce/index.html', context)

def programsDetail(request, program_id):
    program = get_object_or_404(TrainingProgram, pk=program_id)
    attendees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=program_id)
    number = attendees.values().annotate(employeeCount=Count('employee_id'))
    # print("number: ", employees)
    print("attendees: ", attendees.values())
    # print("attendees values: ", attendees.values())
    # print("attendees.get: ", attendees.get('employee_id'))
    # print("items: ", attendees.items())

    # way #1
    # employees = Employee.objects.filter(pk=attendees[0:1].values('employee_id'))

# note: gotta match the employee_id from attendees to the pk of employee

# way #2
    attendee_list = attendees.values('employee_id')
    print("attendee list: ", attendee_list[0:2])
    # employees = Employee.objects.all()
    # print("employees values: ", employees.values())
    # filtered = employees.filter(id=attendee_list)
    # print(filtered)
    # employees = Employee.objects.filter(id=attendee_list[0:1])


# way #3
    # idList = []
    # idDict = { 'ids': idList}

    # for id in attendee_list:
    #     ids = id.get('employee_id')
    #     # idDict["id"] = ids
    #     idList.append(ids)
    #     print("id: ", id)
    #     print("ids: ", ids)
    #     employees = Employee.objects.filter(id=id.get('employee_id'))


    # print("list: ", idList)
    # print("dict: ", idDict)
    # print("dict values: ", idDict.get('ids'))


    # attendees = get_object_or_404(EmployeeTrainingProgram, trainingProgram_id=program_id)
    # employees = Employee.objects.filter(id=attendee.values('employee_id'))
    # print(employees)


    context = {'program': program, 'attendees': attendees}
    # print(employees)
    return render(request, 'workforce/programDetail.html', context)