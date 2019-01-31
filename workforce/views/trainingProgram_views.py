from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from ..models import TrainingProgram


def trainingList(request):
    '''
    Summary:
        [this method filters through the TrainingProgram table by the startDate and provides the instances where the startDate is in the FUTURE when compared to the current time.]

    Author:
        Dillon Williams

    Arguments:
        request: The render() shortcut renders templates with a request context. Template context processors take the request object and return a dictionary which is added to the context.

    Returns:
        Returns a list of the current training programs.
    '''
    currentTime = timezone.now()
    training_list = TrainingProgram.objects.filter(startDate__gte=currentTime)
    context = {'training_list': training_list}
    return render(request, 'workforce/trainingProgram_list.html', context)


def newTraining(request):
    '''Will check to see if the request is a POST and if not it will render our form

    Arguments:
    request: Template context processors take the request object and return a dictionary which is added to the context.

    Returns:
    render: this will render our form in the browser
    HttpResponseRedirect: this will redirect the user back to training program list page

    '''


    if request.method != 'POST':
        return render(request, 'workforce/trainingProgram_add.html')
    else:
        progName = request.POST['trainName']
        startDate = request.POST['trainStart']
        endDate = request.POST['trainEnd']
        maxAttendees = request.POST['trainMax']
        obj = TrainingProgram(name=progName.title(), startDate=startDate, endDate=endDate, maxAttendees=maxAttendees)
        obj.save()
        return HttpResponseRedirect(reverse('workforce:training'))

def pastTrainingList(request):
    '''
    Summary:
        [this method filters through the TrainingProgram table by the startDate and provides the instances where the startDate is in the past when compared to the current time.]

    Author:
        Dillon Williams

    Arguments:
        request: The render() shortcut renders templates with a request context. Template context processors take the request object and return a dictionary which is added to the context.

    Returns:
        Returns a list of the PAST training programs.
    '''

    currentTime = timezone.now()
    past_training_list = TrainingProgram.objects.filter(startDate__lte=currentTime)
    context = {'past_training_list': past_training_list}
    return render(request, 'workforce/pastTrainingPrograms.html', context)

