from django.shortcuts import render, get_object_or_404
from myunisite.models import Program, Department


# Create your views here.
def main_page_view(request):
    return render(request, 'main_page.html', {})


def program_list(request):
    all_programes = Program.objects.all()
    context = {'programs': all_programes}
    return render(request, 'program_list.html', context)


def program_detail(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    context = {'programs': program}
    return render(request, 'program_detail.html', context)


def department_list(request):
    all_departments = Department.objects.all()
    context = {'departments': all_departments}
    return render(request, 'deparment_list.html', context)


def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    context = {'departments': department}
    return render(request, 'deparment_detail.html', context)

