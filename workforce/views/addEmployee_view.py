from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Employee

def addEmployee(request):
    if request.method != 'POST':
        return render(request, 'workforce/addEmployee.html')
    else:
        progName = request.POST['trainName']
        startDate = request.POST['trainStart']
        endDate = request.POST['trainEnd']
        maxAttendees = request.POST['trainMax']
        obj = TrainingProgram(name=progName.title(), startDate=startDate, endDate=endDate, maxAttendees=maxAttendees)
        obj.save()
        return HttpResponseRedirect(reverse('workforce:training'))
