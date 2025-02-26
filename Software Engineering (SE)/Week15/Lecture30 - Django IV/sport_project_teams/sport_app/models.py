from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    """
    Model representing a user's registration for a sports team.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Allow multiple registrations per user
    sport = models.CharField(max_length=25)
    team_name = models.CharField(max_length=30)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sport', 'team_name'], name='unique_team_per_sport')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.team_name} ({self.sport})"
