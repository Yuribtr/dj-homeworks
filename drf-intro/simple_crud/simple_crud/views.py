import os
from django.shortcuts import render


def main_page(request):
    template = f'simple_crud{os.sep}index.html'
    context = {}
    return render(request, template, context)
