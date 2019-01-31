from django.shortcuts import render, get_object_or_404
from ..models import TrainingProgram, EmployeeTrainingProgram

def programsDetail(request, program_id):
    '''Will display details for a single Training Program 
    
    Arguments:
        request: Template context processors take the request object and return a dictionary which is added to the context.
        program_id: the id for a specific training program
    
    Returns:
        Takes a user to a specific program's detail page
    '''

    # go to training program and get the program info for the program with the id that matches program_id
    program = get_object_or_404(TrainingProgram, pk=program_id)
    # go to our join table filter through and find any rows where the ids match
    attendees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=program_id)
    context = {'program': program, 'attendees': attendees}
    return render(request, 'workforce/programDetail.html', context)
