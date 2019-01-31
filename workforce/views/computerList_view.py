from django.shortcuts import render, get_object_or_404

def computerList(request):
        return render(request, 'workforce/computers.html')