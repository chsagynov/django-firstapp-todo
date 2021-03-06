# Generated by Django 2.0.1 on 2018-01-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_card_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='done_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
