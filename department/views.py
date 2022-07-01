from django.shortcuts import render, redirect
from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee


# Create your views here.
def DepartmentList(request):
    departments = Department.objects.all()
    return render(request, 'department/departmentlist.html', {'departments': departments})

def AddDepartment(request):
    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department-list')

    return render(request, 'department/adddepartment.html', {'form': form})

def DepartmentDetail(request, id):
    departmentdetail = Department.objects.get(id=id)
    position = departmentdetail.id
    employee = Employee.objects.filter(position = position)
    return render(request, 'department/departmentdetail.html',
     {'departmentdetail': departmentdetail, 'employee': employee})


def EmployeeList(request, id):
    employees = Employee.objects.all()
    return render(request, 'department/departmentdetail.html', {'employees':employees})

def AddEmployee(request, id):
    form = EmployeeForm(initial={'position': id})

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department-detail', id=id)

    return render(request, 'department/addemployee.html', {'form': form})


def Edit(request, id):
    department = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None, instance = department)
    if form.is_valid():
        form.save()
        return redirect('department-list')

    return render(request, 'department/edit.html', {'form':form, 'department': department})


def Delete(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('department-list')

def Edit2(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance = employee)
    if form.is_valid():
        form.save()
        return redirect('department-list')

    return render(request, 'department/edit2.html', {'form':form, 'employee': employee})


def Delete2(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('department-list')