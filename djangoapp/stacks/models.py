import uuid

from django.db import models


class Stack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    squads = models.ManyToManyField(
        'squads.Squad',
        through='StackOnSquad',
        related_name='stacks')

    def __str__(self) -> str:
        return f'{self.name}'


class StackOnSquad(models.Model):
    stack = models.ForeignKey('Stack', on_delete=models.CASCADE)
    squad = models.ForeignKey('squads.Squad', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['stack', 'squad'],
                name='stack_on_squad_unique'),
        ]

    def __str__(self) -> str:
        return f'{self.stack.name} on {self.squad.name}'
