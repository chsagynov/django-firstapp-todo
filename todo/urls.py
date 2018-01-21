from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.CardListView.as_view(), name='cardlist'),
    path('add/', views.add_card, name='add_card'),
    path('<int:card_id>/delete/', views.del_card, name='del_card'),
    path('<int:card>/add_task/', views.add_task, name='add_task'),
    path('<int:task_id>/delete_task/', views.del_task, name='del_task'),
    path('<int:task_id>/mark_task/', views.mark_task, name='mark_task'),
]