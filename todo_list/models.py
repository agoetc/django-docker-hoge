from django.db import models
import uuid as uuid_lib


class Todo(models.Model):
    todo = models.CharField(max_length=256)


class Profile(models.Model):
    profile_id = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    email_address = models.EmailField(max_length=254, unique=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)


class Customer(models.Model):
    customer_id = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
