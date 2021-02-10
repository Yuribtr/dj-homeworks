from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = [*Phone.objects.all()]
    phones.sort(key=lambda x: x.price, reverse=True)
    context = {'phones': phones}
    return render(
        request,
        template,
        context
    )
