import datetime

from django.db import models
from django.utils import timezone


class Card(models.Model):
    card_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.card_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def incomplete_tasks(self):
        # Count all incomplete tasks on the current list instance
        return Task.objects.filter(list=self, done=0)

class Task(models.Model):
    card = models.ForeignKey(Card,
    	on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    task_text = models.CharField(max_length=200)
    done = models.BooleanField(default=None)
    done_date = models.DateTimeField(blank=True, null=True)

    def save(self):
        if self.done:
            self.done_date = datetime.datetime.now()
        super(Task, self).save()

    def __str__(self):
        return self.task_text