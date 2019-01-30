from django.urls import path

# from workforce import views
# from .views import departmentDetail_view
# from .views import views
# from .views import __init__
from . import views

app_name = 'workforce'

# urlpatterns = [
#     path('', departmentDetail_view.index, name='index'),
#     path('departments/<int:department_id>/', departmentDetail_view.detail, name='departmentDetail')
# ]

urlpatterns = [
    path('', views.index, name='index'),
	path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('departments/', views.departmentList, name='departmentList'),
    path('departmentDetail/<int:department_id>/', views.detail, name='departmentDetail'),
    path('programs/<int:program_id>/', views.programsDetail, name="programsDetail"),
    path('training/', views.trainingList, name='training'),
    path('addtraining/', views.newTraining, name='addTraining')
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





