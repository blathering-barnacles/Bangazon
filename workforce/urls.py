from django.urls import path

from workforce import views

app_name = 'workforce'

urlpatterns = [
    path('<int:employee_id>/', views.employeeDetail, name='employeeDetail'),
    path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
]

