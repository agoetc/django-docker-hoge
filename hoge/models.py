from django.db import models
from todo_list.models import Customer


class Hoge(models.Model):
    hoge = models.CharField(max_length=256)

    customer = models.ForeignKey(
        Customer,
        related_name='hoges',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
