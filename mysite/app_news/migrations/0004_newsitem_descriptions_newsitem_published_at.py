# Generated by Django 4.2.1 on 2023-06-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_newssource_newsitem_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='descriptions',
            field=models.TextField(default='', verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='дата публикации'),
        ),
    ]
