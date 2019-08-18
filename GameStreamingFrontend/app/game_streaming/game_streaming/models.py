from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# python3 manage.py makemigrations game_streaming

game_id_validator = RegexValidator(r'\w+', "The only available chars are: a-z, A-Z, 0-9 and '_'")
image_version_validator = RegexValidator(r'\d+([\.\-_]\d+)*',
        "Version number is made using digits possibly separated by '.', '-' or '_'")

class Game(models.Model):
    id = models.CharField('Game ID', max_length=20, primary_key=True, validators=[game_id_validator])
    name = models.CharField('The name of the game', max_length=80)
    description_short = models.TextField('Short description of the game', max_length=120, blank=True)
    description = models.TextField('Description of the game', max_length=500, blank=True)
    developer = models.CharField('The developer of the game', max_length=40)
    publisher = models.CharField('The publisher of the game', max_length=40)
    is_available = models.BooleanField('Whether the game is available for purchase or not', default=False)
    is_hidden = models.BooleanField('Whether the game is hidden in the store of not', default=False)
    image_cover = models.CharField('URI to the game cover image', max_length=300, blank=True)
    image_banner = models.CharField('URI to the game banner image', max_length=300, blank=True)

    def __str__(self):
        return self.name

class UserLibraryGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_on = models.DateField('The date the user added the game to its library', auto_now=True)

    def __str__(self):
        return '{}: {}'.format(str(self.user), str(self.game))

class GameImage(models.Model):
    name = models.CharField("Name of the image", max_length=50)
    version = models.CharField("Version of the image", max_length=10, unique=True, validators=[image_version_validator])
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return '{}:{}'.format(self.name, self.version)

class GameContainer(models.Model):
    id = models.CharField("Container ID", max_length=64, primary_key=True)
    name = models.CharField("Container name", max_length=32)
    image = models.ForeignKey(GameImage, on_delete=models.CASCADE, related_name='containers')
    is_in_use = models.BooleanField("Whether the container is used at this time")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='containers')

    def __str__(self):
        return '{} ({})'.format(self.name, str(self.image))
