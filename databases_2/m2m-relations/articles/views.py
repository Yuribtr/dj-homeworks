from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    articles = [*Article.objects.order_by('-published_at').prefetch_related('scopes__articles', 'scopes')]
    context = {'object_list': articles}
    return render(request, template, context)
