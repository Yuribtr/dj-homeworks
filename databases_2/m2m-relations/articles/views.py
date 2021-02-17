from django.db.models import Prefetch
from django.shortcuts import render
from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    articles = [*Article.objects.order_by('-published_at').prefetch_related(
        Prefetch(
            'scopes',
            queryset=ArticleScope.objects.select_related(
                'scope'
            ).order_by('-is_main'),
        ),
    )]
    context = {'object_list': articles}
    return render(request, template, context)
