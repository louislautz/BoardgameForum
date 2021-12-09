from django.db import models

class Boardgamer(models.Model):
    """Defines a Forum user"""
    biography = models.CharField(max_length=300)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string that describes the user"""
        return self.biography


class Game(models.Model):
    """Defines a Game object"""
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(Boardgamer, on_delete=models.CASCADE)
    availability = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        message = f"{self.name} by {self.owner}\n Added: {self.date_added} \n"
        if self.availability:
            message += "Currently available"
        else:
            message += "NOT available"
        
        return message
            
