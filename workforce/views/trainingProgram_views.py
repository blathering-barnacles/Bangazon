from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import TrainingProgram


def trainingList(request):
    training_list = TrainingProgram.objects.order_by('name')
    return render(request, 'workforce/trainingProgram_list.html', {'training_list': training_list})

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


    

 
