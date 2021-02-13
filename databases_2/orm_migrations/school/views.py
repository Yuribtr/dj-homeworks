from django.views.generic import ListView
from django.shortcuts import render
from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = [*Student.objects.order_by('group').prefetch_related('teachers')]
    context = {'object_list': students}
    return render(request, template, context)
