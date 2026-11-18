
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm


# Display all employees
def employee_list(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }

    return render(request, 'home.html', context)


# Display individual employee details
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    context = {
        'employee': employee,
    }

    return render(request, 'employee_detail.html', context)


# Add new employee
def add_employee(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    context = {
        'form': form,
    }

    return render(request, 'add_employee.html', context)


# Edit existing employee
def edit_employee(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect('employee_detail', id=employee.id)

    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'employee': employee,
    }

    return render(request, 'edit_employee.html', context)


# Delete employee

def delete_employee(request, id):
    # print("========== DELETE DEBUG ==========")
    # print("Request method:", request.method)
    # print("Employee ID:", id)

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()

        # print("Deleted employee:", employee.full_name)
        # print("Remaining employees:", Employee.objects.count())

        return redirect('employee_list')

    print("Invalid request method")
    return redirect('employee_list')