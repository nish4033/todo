from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(
        max_length=249, null=False, blank=False, unique=True
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"


class Task(models.Model):
    STATUS_CHOICE = (
        ("P", "Pending"),
        ("C", "Completed"),
    )
    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        blank=True,
        null=True,
        default="Pending",
    )
    description = models.CharField(max_length=249, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE, db_column="user_id")
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tasks"


class Token(models.Model):
    token = models.CharField(
        max_length=249, blank=False, null=False, unique=True
    )
    user = models.ForeignKey(User, models.CASCADE, db_column="user_id")
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()
