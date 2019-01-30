from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import TrainingProgram


def trainingList(request):
    training_list = TrainingProgram.objects.order_by('name')
    return render(request, 'workforce/trainingProgram_list.html', {'training_list': training_list})

def newTraining(request):
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
    

 
