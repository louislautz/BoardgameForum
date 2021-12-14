from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Game(models.Model):
    """Defines a Game object"""
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_available(self):
        return self.availability
            
