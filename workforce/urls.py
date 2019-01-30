from django.urls import path

from workforce import views

app_name = 'workforce'

urlpatterns = [
    path('<int:employee_id>/', views.employeeDetail, name='employeeDetail'),

]


