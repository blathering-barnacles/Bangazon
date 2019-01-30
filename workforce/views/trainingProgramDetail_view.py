from django.shortcuts import render, get_object_or_404
from ..models import TrainingProgram, EmployeeTrainingProgram

def programsDetail(request, program_id):
    # go to training program and get the program info for the program with the id that matches program_id
    program = get_object_or_404(TrainingProgram, pk=program_id)
    # go to our join table filter through and find any rows where the ids match
    attendees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=program_id)
    context = {'program': program, 'attendees': attendees}
    return render(request, 'workforce/programDetail.html', context)
