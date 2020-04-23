from django.urls import path
from employee import views

#

urlpatterns = [
    path('', views.employeeform, name='employee_form'),
    path('list', views.list, name='employee_list'),
    path('update/<int:id>', views.update, name='employee_update'),
    path('delete/<int:id>', views.delete, name='employee_delete'),



]
