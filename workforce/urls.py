from django.urls import path

# from workforce import views
# from .views import departmentDetail_view
from .views import views

app_name = 'workforce'

# urlpatterns = [
#     path('', departmentDetail_view.index, name='index'),
#     path('<int:department_id>/', departmentDetail_view.detail, name='detail')
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:department_id>/', views.detail, name='departmentDetail')
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