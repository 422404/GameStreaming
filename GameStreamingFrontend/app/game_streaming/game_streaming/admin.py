from django.contrib import admin
from .models import Game, UserLibraryGame, GameImage, GameContainer

admin.site.register(Game)
admin.site.register(UserLibraryGame)
admin.site.register(GameImage)
admin.site.register(GameContainer)
