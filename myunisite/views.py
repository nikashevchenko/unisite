from django.shortcuts import render, get_object_or_404

from myunisite.models import Programs, Departments


# Create your views here.
def main_page_view(request):
    return render(request, 'main_page.html', {})


def program_list(request):
    all_programes = Programs.objects.all().order_by('-created_at')
    context = {'programs': all_programes}
    return render(request, 'program_list.html', context)


def program_detail(request, program_id):
    program = get_object_or_404(Programs, pk=program_id)
    context = {'program': program}
    return render(request, 'program_detail.html', context)


def department_list(request):
    all_departments = Departments.objects.all().order_by('-created_at')
    context = {'departments': all_departments}
    return render(request, 'deparments_list.html', context)


def department_detail(request, department_id):
    department = get_object_or_404(Departments, pk=department_id)
    context = {'department': department}
    return render(request, 'deparment_detail.html', context)
