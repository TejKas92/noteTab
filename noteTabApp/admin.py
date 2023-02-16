from django.contrib import admin

from .models import *

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ['student', 'note']
    search_fields = ['student']
admin.site.register(Note, NoteAdmin)
