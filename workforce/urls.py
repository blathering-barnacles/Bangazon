from django.urls import path

from workforce import views

app_name = 'workforce'
urlpatterns = [
    path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('employees/<int:employee_id>/', views.employeeDetail, name='employeeDetail'),
    path('departments/', views.departmentList, name='departmentList'),
    path('training/', views.trainingList, name='training'),
    path('addtraining/', views.newTraining, name='addTraining'),
    path('programs/<int:program_id>/', views.programsDetail, name='programsDetail')
]

# example from DjangoMusic Exercise
# urlpatterns = [
#     # ex: /artists/
#     path('', views.index, name='index'),
#     # ex: /artists/5/
#     path('<int:artist_id>/', views.detail, name='detail'),
#     path('postartist/', views.addArtistForm, name='addArtistForm'),
#     path('postartist/submittal/', views.postartist, name='postartist')
# ]





