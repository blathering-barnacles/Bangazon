from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Employee, Department
from django.db import connection


def addEmployee(request):
    '''
    [Method is used to take information sent from the template and post a new employee to the employee table.]
    TICKET 2: R Lancaster

    Arguments:
        request

    Returns:
        [redirect] -- successful completion of object saving to table will redirect the user to the list of employees.
    '''
    # if request.method == 'GET':
    #     # get the departments so that names can display in the dropdown menu
    #     department_list = Department.objects.all()
    #     context = {"department_list" : department_list}

    #     #render the form page
    #     return render(request, 'workforce/addEmployee.html', context)
    # elif request.method == 'POST':
    #     firstName = request.POST['firstName']
    #     lastName = request.POST['lastName']
    #     startDate = request.POST['startDate']
    #     isSupervisor = request.POST['isSupervisor']
    #     department = request.POST['department']
    #     departmentName = Department.objects.get(id=department)
    #     obj = Employee(firstName=firstName.title(), lastName=lastName.title(), startDate=startDate, isSupervisor=isSupervisor, department=departmentName)
    #     obj.save()
    #     return HttpResponseRedirect(reverse('workforce:employeeList'))
    if request.method == 'GET':
        department_list = Department.objects.raw('SELECT * FROM workforce_department')
        context = {'department_list': department_list}
        return render (request, 'workforce/addEmployee.html', context)

    elif request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        startDate = request.POST['startDate']
        isSupervisor = request.POST['isSupervisor']
        department = request.POST['department']

        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO workforce_employee VALUES(%s, %s, %s, %s, %s, %s)', [None, firstName, lastName, startDate, isSupervisor, department])

        return HttpResponseRedirect(reverse('workforce:employeeList'))



# def songNew(request):
#   if request.method == "GET":
#     albums = Album.objects.raw("SELECT * FROM history_album")
#     artists = Artist.objects.raw("SELECT * FROM history_artist")
#     context = {
#         "route": "history:song_new",
#         "albums": albums,
#         "artists": artists
#     }
#     return render(request, 'history/song_form.html', context)

#   if request.method == "POST":
#     title = request.POST["title"] # This will be a string
#     artist = request.POST["artist"] # This will be an id

#     # WITH THE ORM
#     # Go get an instance of the artist so we can save it as foreign key on song
#     # ar = Artist.objects.get(id=artist)
#     # Shorthand way makes instance and saves at same time
#     # Song.objects.create(title=title, artist=artist)

#     # WITH RAW SQL USING DIRECT CONNECTION VIA CURSOR
#     with connection.cursor() as cursor:
#       cursor.execute("INSERT into history_song VALUES(%s, %s, %s)", [None, title, artist])
#       new_song_id = cursor.lastrowid
#       print("New song id after adding new song", new_song_id)

#       # Now, save the album(s) to join table, since song/album is many-to-many
#       addSongAlbum(request.POST.getlist("albums"), new_song_id)

#       return HttpResponseRedirect(reverse('history:songs'))