# Generated by Django 4.2.1 on 2023-06-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homesale', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Homes'},
        ),
        migrations.AlterModelOptions(
            name='hometype',
            options={'verbose_name': 'Home Type', 'verbose_name_plural': 'Home Types'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='roomsamount',
            options={'verbose_name': 'Rooms Amount', 'verbose_name_plural': 'Rooms Amount'},
        ),
    ]
