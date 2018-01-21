from django.contrib import admin
from todo.models import Card, Task


class TaskInline(admin.TabularInline):
    fields=('task_text', 'done')
    model = Task
    extra = 3


class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['card_text']}),
    ]
    inlines = [TaskInline]
    list_display = ('card_text', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['card_text']

class TaskAdmin(admin.ModelAdmin):
    list_display = ('card', 'task_text', 'done', 'done_date')
    list_filter = ('card',)
    ordering = ('card',)
    search_fields = ('tast_text',)

admin.site.register(Card, CardAdmin)
admin.site.register(Task, TaskAdmin)