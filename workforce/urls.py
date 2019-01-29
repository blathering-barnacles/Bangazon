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
    path('departments/<int:department_id>/', views.detail, name='departmentDetail')
]

# urlpatterns = [
#     path('', departmentDetail_view.index, name='index'),
#     path('departments/<int:department_id>/', departmentDetail_view.detail, name='departmentDetail')
# ]