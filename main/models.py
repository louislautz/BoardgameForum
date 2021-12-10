from django.db import models

class Boardgamer(models.Model):
    """Defines a Forum user"""
    username = models.CharField(max_length=50)
    biography = models.CharField(max_length=300)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string that describes the user"""
        return self.username


class Game(models.Model):
    """Defines a Game object"""
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(Boardgamer, on_delete=models.CASCADE)
    availability = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
            
