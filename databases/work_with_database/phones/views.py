from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = [*Phone.objects.order_by('-release_date').all()]
    sort_param = request.GET.get('sort', None)
    sort_directions = {'sort_date': '', 'sort_min_price': '', 'sort_max_price': '', 'sort_name': ''}
    if sort_param:
        if sort_param == 'min_price':
            sort_directions['sort_min_price'] = 'disabled'
            phones.sort(key=lambda x: x.price, reverse=False)
        elif sort_param == 'max_price':
            sort_directions['sort_max_price'] = 'disabled'
            phones.sort(key=lambda x: x.price, reverse=True)
        elif sort_param == 'name':
            sort_directions['sort_name'] = 'disabled'
            phones.sort(key=lambda x: x.name, reverse=False)
        else:
            sort_directions['sort_date'] = 'disabled'
    else:
        sort_directions['sort_date'] = 'disabled'
    context = {'phones': phones, **sort_directions}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Phone not found')
    context = {'phone': phone}
    return render(request, template, context)
