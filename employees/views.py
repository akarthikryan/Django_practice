from django.shortcuts import render, get_object_or_404
from .models import Employee

# Decided which url pattern to create
# Created URL pattern in the main urls.py and forwarded it to employees.urls
# Created the view
# Created the template

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    context = {
        'employee': employee,
    }
    return render(request, 'employee_detail.html', context)


def add_employee(request):
    return render(request, 'add_employee.html')