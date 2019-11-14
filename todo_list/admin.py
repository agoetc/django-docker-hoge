from django.contrib import admin

from .models import Todo, Customer, Profile


@admin.register(Todo)
class Todo(admin.ModelAdmin):
    pass


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    pass


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    pass
