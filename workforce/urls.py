from django.urls import path 

from workforce import views
from . import views

app_name = 'workforce'
urlpatterns = [
    path('departments/', views.departmentList, name='departmentList')
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