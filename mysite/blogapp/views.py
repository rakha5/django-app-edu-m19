from django.views.generic import ListView

from .models import Article

import logging

logger = logging.getLogger(__name__)


class ArticlesListView(ListView):
    template_name = 'blogapp/article_list.html'
    # model = Article
    context_object_name = 'articles'
    queryset = (
        Article.objects.select_related(
            'author'
        ).prefetch_related(
            'category', 'tags'
        ).defer(
            'content',
        )
    )

    def get(self, request, *args, **kwargs):
        logger.info('Запрошена страница со списком статей.')
        logger.debug('TEST!!!!!!!!.')
        return super().get(request, *args, **kwargs)
