# Generated by Django 2.0.1 on 2018-01-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180120_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
