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
    startDate = str(program.startDate)
    startDateNonString = program.startDate
    endDate = str(program.endDate)
    print("program start date: ", program.startDate)
    print("program end date: ", program.endDate)
    # go to our join table filter through and find any rows where the ids match
    attendees = EmployeeTrainingProgram.objects.filter(trainingProgram_id=program_id)
    td = timedelta(days=4)

    if endDate <= startDate:
        endDate = str(startDateNonString + td)
        print("new end date: ", endDate)

    context = {'program': program, 'attendees': attendees, 'startDate': startDate, 'endDate': endDate}
    print(context)
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

    program = TrainingProgram.objects.get(id=program_id)
    # print("program :", program.id)
    # print("program: ", program.values())
    # print("new name value: ", request.POST['programName'])
    program.name = request.POST['programName']
    # program.startDate = request.POST['startDate']
    # print("program.startDate: ", program.startDate)
    td = timedelta(days=2)
    dates = datetime.now()
    dateTest = dates + td
    print("dates: ", str(dates)[0:10])
    print("td: ", td)
    print("date Test: ", dateTest)
    endDateFilter = request.POST['endDate']
    startDateFilter = request.POST['startDate']
    test = startDateFilter + " " + "00:00:00"
    newtest = str(test)
    intTest = datetime.fromisoformat(newtest)
    # intTest = int(newtest)
    print("new test: ", newtest)
    print("TEST: ", str(intTest + td)[0:13])

    # If the date typed in startDate is less than todays date then it grabs todays date and puts that there.
    if startDateFilter <= str(dates)[0:10]:
        print("it passed!")
        todaysDate = str(dates)[0:10]
        program.startDate = todaysDate
    else:
        print("it failed")
        program.startDate = startDateFilter


    # If the date typed in on endDate is less than the start date then it grabs todays time and adds 4 days
    # if endDateFilter <= str(program.startDate):
    # print("it passed")
    # futureDate = str(dates + td)
    # print("future date: ", futureDate[0:10])
    # program.endDate = futureDate[0:10]
    # print("date lesser than start date: ", program.startDate)
    # else:
    # program.endDate = endDateFilter
    # print("it failed")

    # If the date entered in endDate is less than the date entered in startDate then it transforms and formats the
    # startDate into a number and it adds 2 days. That new date will then be added as an endDate.
    if endDateFilter <= startDateFilter:
        print("it passed")
        makeStartDate = startDateFilter + " " + "00:00:00"
        formatedStartDate = datetime.fromisoformat(makeStartDate)
        futureDate = str(formatedStartDate + td)
        program.endDate = futureDate[0:10]
    else:
        print("it failed")
        program.endDate = endDateFilter



    program.maxAttendees = request.POST['maxAttendees']
    program.save()
    return HttpResponseRedirect(reverse('workforce:programsDetail', args=(program.id,)))