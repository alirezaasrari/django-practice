from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentList, name='department-list'),
    path('adddepartment/', views.AddDepartment, name='add-department-form'),
    path('departmentdetail/<int:id>', views.DepartmentDetail, name='department-detail'),
    path('addemployee/<int:id>', views.AddEmployee, name='add-employee-form'),
    path('employeelist/<int:id>', views.EmployeeList, name='employee-list'),
    path('deletecase/<int:id>', views.Delete, name='deletecase'),
    path('editcase/<int:id>', views.Edit, name='editcase'),
    path('deletecase2/<int:id>', views.Delete2, name='deletecase2'),
    path('editcase2/<int:id>', views.Edit2, name='editcase2'),
]