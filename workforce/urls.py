from django.urls import path 

from workforce import views
from . import views

app_name = 'workforce'
urlpatterns = [
    path('training/', views.trainingList, name='training'),
    path('addtraining/', views.newTraining, name='addTraining')
]


