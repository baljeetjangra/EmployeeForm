from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import *
# Create your views here.


def employeeform(request, id=0):
    if id == 0:
        form = EmployeeForm()
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/list')

    context = {
        'form': form
    }
    return render(request, 'employee/employeeform.html', context)


def list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employee/list.html', context)


def update(request, id):
    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(instance=employee)
    if id != 0:
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('/list')
    context = {
        'form': form
    }
    return render(request, 'employee/employeeform.html', context)


def delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
