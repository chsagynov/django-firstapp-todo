from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from todo.forms import AddCardForm, AddTaskForm

from .models import Card, Task

class CardListView(generic.ListView):
    template_name = 'todo/card_lists.html'
    context_object_name = 'latest_card_list'

    def get_queryset(self):
        """Return the last five published cards."""
        return Card.objects.order_by('pub_date')


def add_card(request):
    if request.POST:
        form = AddCardForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "A new card has been added.")
                HttpResponseRedirect(reverse('todo:cardlist', ))
            except IntegrityError:
                messages.error(
                    request,
                    "There was a problem saving the new card. ")
    else:
        messages.error(
            request,
            "No post data. ")

    return HttpResponseRedirect(reverse('todo:cardlist', ))


def del_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)

    if request.method == 'GET':
        card.delete()
        messages.success(request, "{card_text} is gone.".format(card_text=card.card_text))
        return HttpResponseRedirect(reverse('todo:cardlist'))
    else:
        card_count_done = Task.objects.filter(card_id=card.id, done=1).count()
        card_count_undone = Task.objects.filter(card_id=card.id, done=0).count()
        card_count_total = Task.objects.filter(card_id=card.id).count()

    return HttpResponseRedirect(reverse('todo:cardlist'))


def del_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'GET':
        task.delete()
        messages.success(request, "{task_text} is gone.".format(task_text=task.task_text))
        return HttpResponseRedirect(reverse('todo:cardlist'))

    return HttpResponseRedirect(reverse('todo:cardlist'))

def mark_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    task.done = not task.done
    task.save()

    return HttpResponseRedirect(reverse('todo:cardlist'))


def add_task(request, card):
    if request.POST:
        form = AddTaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "A new task has been added.")
                HttpResponseRedirect(reverse('todo:cardlist', ))
            except IntegrityError:
                messages.error(
                    request,
                    "There was a problem saving the new task. ")
    else:
        messages.error(
            request,
            "No post data. ")

    #form = AddTaskForm(card_id);

    return HttpResponseRedirect(reverse('todo:cardlist', ))