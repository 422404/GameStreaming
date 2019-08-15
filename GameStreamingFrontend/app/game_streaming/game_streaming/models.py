from django.db import models

# python3 manage.py makemigrations game_streaming

class Game(models.Model):
    id = models.CharField('Game ID', max_length=20, primary_key=True)
    name = models.CharField('The name of the game', max_length=80)
    description = models.TextField('Description of the game', max_length=500)
    editor = models.CharField('The editor of the game', max_length=40)
    publisher = models.CharField('The publisher of the game', max_length=40)
    is_available = models.BooleanField('Whether the game is available for purchase or not', default=False)
    is_hidden = models.BooleanField('Whether the game is hidden in the store of not', default=False)
    image_cover = models.CharField('URI to the game cover image', max_length=300, blank=True)
    image_banner = models.CharField('URI to the game banner image', max_length=300, blank=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
