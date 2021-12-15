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
            

class Rent(models.Model):
    """Defines a game renting"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    rent_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f"{self.renter.username} rented {self.game.name}"

    def is_returned(self):
        return self.returned