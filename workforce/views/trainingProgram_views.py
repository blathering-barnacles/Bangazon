from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from ..models import TrainingProgram


def trainingList(request):
    currentTime = timezone.now()
    training_list = TrainingProgram.objects.filter(startDate__gte=currentTime)
    context = {'training_list': training_list}
    return render(request, 'workforce/trainingProgram_list.html', context)


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
    
def pastTrainingList(request):
    currentTime = timezone.now()
    past_training_list = TrainingProgram.objects.filter(startDate__lte=currentTime)
    context = {'past_training_list': past_training_list}
    return render(request, 'workforce/pastTrainingPrograms.html', context)

