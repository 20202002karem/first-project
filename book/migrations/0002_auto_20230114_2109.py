# Generated by Django 3.0 on 2023-01-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='num_of_pages',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
    ]
