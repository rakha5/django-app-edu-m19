# Generated by Django 4.2.1 on 2023-06-01 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('code', models.CharField(max_length=64, verbose_name='код')),
            ],
            options={
                'verbose_name': 'тип новостей',
                'verbose_name_plural': 'типы новостей',
            },
        ),
        migrations.AddField(
            model_name='newsitem',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='app_news.newstype'),
        ),
    ]
