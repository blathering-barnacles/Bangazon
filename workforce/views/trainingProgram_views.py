from django.shortcuts import get_object_or_404, render
from ..models import TrainingProgram



def trainingList(request):
    training_list = TrainingProgram.objects.order_by('name')
    return render(request, 'workforce/trainingProgram_list.html', {'training_list': training_list})


# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# from .models import Artists


# def index(request):
#   latest_artist = Artists.objects.order_by('name')
#   context = {
#     'latest_artist': latest_artist,
#   }
#   return render(request, 'artists/index.html', context)

# # Define a view to return a template that displays the details of a 
# # specific artist, and list all of the songs related to that artist.

# def detail(request, artistid_id):
#     artist = get_object_or_404(Artists, pk=artistid_id)   
#     return render(request, 'artists/detail.html', {'artist': artist})

# def newArtist(request):
#   title = request.POST['artistName']
#   est = request.POST['artistEstablished']
#   q = Artists(name=title.title(), established=est.title())
#   q.save()
#   return HttpResponseRedirect(reverse('history:index'))

 
