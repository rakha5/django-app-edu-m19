from django.core.management import BaseCommand

from blogapp.models import Article, Author, Category, Tag


class Command(BaseCommand):
    """
    Create articles
    """

    def handle(self, *args, **options):
        self.stdout.write('Create articles')
        count = 0

        while count < 1000:
            articles = [
                ('Article10', 'top article',
                 Author.objects.get(pk=1), Category.objects.get(pk=1),),
                ('Article20', 'wow article',
                 Author.objects.get(pk=2), Category.objects.get(pk=2),),
                ('Article30', 'super article',
                 Author.objects.get(pk=3), Category.objects.get(pk=3),),
            ]

            for title, content, author, category in articles:
                article = Article.objects.create(
                    title=title,
                    content=content,
                    author=author,
                    category=category,
                )
                article.tags.set([1, 3])
                count += 1
                # self.stdout.write(f'Articles created')

            self.stdout.write(self.style.SUCCESS('Articles created!'))
