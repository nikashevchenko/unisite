from django.db import models

class Programs(models.Model):
    name = models.CharField(max_length=100)
    code =  models.CharField(max_length=100)
    short_description= models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f'Programs: {self.name} {self.short_description} {self.description} ({self.code})'


class Departments(models.Model):
    name = models.CharField(max_length=100)
    department_head = models.CharField(max_length=100)
    programs_list = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
         return f'Departments: {self.name} {self.department_head}'




# Create your models here.
