import uuid
from django.db import models
from users.models import User

# Create your models here.

class Squad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class UsersOnSquads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userRoleOnSquad = models.CharField(max_length=255)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} on {self.squad.name}"

    class Meta:
        verbose_name_plural = "Squads"