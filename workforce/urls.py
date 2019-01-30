from django.urls import path

from workforce import views

app_name = 'workforce'

urlpatterns = [
    path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('employees/<int:employee_id>/', views.employeeDetail, name='employeeDetail'),
]

