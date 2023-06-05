# Generated by Django 4.2.1 on 2023-06-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='home',
            name='square_feet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
