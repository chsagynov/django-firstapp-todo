# Generated by Django 2.0.1 on 2018-01-20 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20180120_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now=True)),
                ('task_text', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=None)),
                ('done_date', models.DateField(blank=True, null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Card')),
            ],
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='card',
        ),
        migrations.DeleteModel(
            name='Checklist',
        ),
    ]
