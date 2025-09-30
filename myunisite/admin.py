from django.contrib import admin
from .models import Program, Teacher, Department, HomepageContent


@admin.register(HomepageContent)
class HomepageContentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

    def has_add_permission(self, request):
        return not HomepageContent.objects.exists()



@admin.register(Program)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "coordinator_name", "issuing_department")
    search_fields = ("name", "code", "coordinator_name")
    list_filter = ("issuing_department",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree")
    search_fields = ("name", "position", "degree")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "department_head")
    search_fields = ("name", "department_head")

# Register your models here.
