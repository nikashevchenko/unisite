from django.db import models
from django.utils.text import Truncator

class HomepageContent(models.Model):
    description = models.TextField(blank=True)
    info = models.TextField(blank=True)
    contacts = models.TextField(blank=True)


class Department(models.Model):
    name = models.CharField(max_length=100)
    department_head = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=255)
    coordinator_contact = models.CharField(max_length=255)
    issuing_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return f'Program: {self.name}  ({self.code})'

    def short_description(self):
        return Truncator(self.description).words(50)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)

    def __str__(self):
        return f'Teacher: {self.name}  ({self.position})'


class Discipline(models.Model):
    name = models.CharField(max_length=200)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="disciplines")

    def __str__(self):
        return f'Discipline: {self.name}'

# Create your models here.
