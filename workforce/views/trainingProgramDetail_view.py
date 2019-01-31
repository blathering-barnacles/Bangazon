from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

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

def editProgramForm(request, program_id):

    '''

    Summary: This function grabs the program from the TraningProgram table that matches with the program_id being
    passed down through the second argument and sticks it in the context.

    It also grabs the start date, and end date from it and converts it into a string. After it has done that it
    passes it into the context to be used in the form, you cannot do it in the template since it will not bring back
    just numbers if you do. If you decide to do program.startDate in template it will bring feb. 02, 2019 which is
    an invalid format.

    Arguments:
    request: Brings back the contents of the template.
    program_id: Brings back the id of the current Traning Program

    Returns:
    [type] -- [description]

    '''

    program = get_object_or_404(TrainingProgram, pk=program_id)
    # You need to pass the program.startDate as a string here for it to be a valid format you can use in your form as a value in the
    # date input. If you decide to do a program.startDate in the form it will be the incorrect format for the input.
    startDate = str(program.startDate)
    endDate = str(program.endDate)
    # attendees variable goes to our join table and filters through and finds any rows where the trainingProgram_id matches
    # the id passed down in the second argument.
    attendees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=program_id)
    context = {'program': program, 'attendees': attendees, 'startDate': startDate, 'endDate': endDate}
    return render(request, 'workforce/programEditForm.html', context)


def editProgram(request, program_id):
    '''

    Summary:
    This Function creates an instance of the current Training Program by going into the TrainingProgram class and
    selecting the program that matches with the program_id being passed down through the second argument.

    It simply re-assigns the properties of that Object to the values that were passed in via the form, and then
    proceeds to just save the new values with the .save() method.

    Arguments:
    request: Brings back the contents of the template.
    program_id: Brings back the id of the current Traning Program

    Returns:
    HttpResponseRedirect: It redirects to the page of that same Training Program so you can see the new changes,
    by using the reverse method and passing the id of the current Training Program.


    '''

    extraDays = timedelta(days=2)
    todaysDate = datetime.now()

    program = TrainingProgram.objects.get(id=program_id)
    program.name = request.POST['programName']

    # Here im not directly sticking the value that has been typed in the form, because I want to do some if statements first,
    # so instead I stick the value inside a variable.

    endDateFilter = request.POST['endDate']
    startDateFilter = request.POST['startDate']


    # If the date typed in startDate in form is less than todays date then it runs this if statement.
    # *Note the todaysDate is in a longer format of yyyy-mm-dd 00:00:00, in order for us to be able to compare it to
    #  the startDateFilter which is in a yyyy-mm-dd format we need to slice it
    # so it only gives us the yyyy-mm-dd.
    if startDateFilter <= str(todaysDate)[0:10]:
        print("it passed!")
        todaysDate = str(todaysDate)[0:10]
        program.startDate = todaysDate
    # If startDate entered in form is not less or equal than todays date then grab it and stick it in the dabases
    # program startDate.
    else:
        print("it failed")
        program.startDate = startDateFilter


    # If the date entered in endDate in form is less than the date entered in startDate then it transforms and formats the
    # startDate into a number and it adds 2 days. That new date will then be added as an endDate.
    if endDateFilter <= startDateFilter:
        print("it passed")

        # In order to go through with this edit the value of the time needs to be in the correct format.
        # The makeStartDate variable is grabing the yyyy-mm-dd format and adding the remaining pieces to it
        # as our first step to transform it to a yyyy-mm-dd 00:00:00 format.
        makeStartDate = startDateFilter + " " + "00:00:00"
        # Now that it has the pieces it needs makeStartDate is still just a string not in a format of time, which is why
        # we need the datetime.fromisoformat() method to transform our string into a datetime format.
        formatedStartDate = datetime.fromisoformat(makeStartDate)
        # The reason we needed it to be in a datetime format is so we can add extra days to it, after that we need to
        # convert it back into a string so we can pass it.
        futureDate = str(formatedStartDate + extraDays)
        # BUT REMEMBER! its still in the yyyy-mm-dd 00:00:00 format so we need to slice it down!
        program.endDate = futureDate[0:10]
    else:
        print("it failed")
        program.endDate = endDateFilter



    program.maxAttendees = request.POST['maxAttendees']
    program.save()
    return HttpResponseRedirect(reverse('workforce:programsDetail', args=(program.id,)))