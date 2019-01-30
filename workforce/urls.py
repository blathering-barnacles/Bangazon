from django.urls import path

from workforce import views

app_name = 'workforce'

# urlpatterns = [
#     path('', departmentDetail_view.index, name='index'),
#     path('departments/<int:department_id>/', departmentDetail_view.detail, name='departmentDetail')
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departmentList, name='departmentList'),
    path('departmentDetail/<int:department_id>/', views.detail, name='departmentDetail'),
	path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('employees/<int:employee_id>/', views.employeeDetail, name='employeeDetail'),
    path('addEmployee/', views.addEmployee, name='addEmployee')
    path('training/', views.trainingList, name='training'),
    path('addtraining/', views.newTraining, name='addTraining'),
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





