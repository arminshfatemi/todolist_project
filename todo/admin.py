from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_time', 'updated_time', 'done_or_not']
    list_display_links = ['id', 'user']
    list_editable = ['done_or_not']
    search_fields = ['id', 'user', 'title']
    list_filter = ['created_time', 'updated_time', 'done_or_not', ]
