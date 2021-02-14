from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    articles = [*Article.objects.order_by('-published_at').select_related('genre', 'author').
        only('text', 'title', 'image', 'author__name', 'genre__name')]
    context = {'object_list': articles}
    return render(request, template_name, context)
