from django.contrib import admin
from hoge.models import Hoge


@admin.register(Hoge)
class Todo(admin.ModelAdmin):
    pass
