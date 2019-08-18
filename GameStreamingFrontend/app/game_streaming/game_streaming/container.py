import secrets
import docker
from .models import GameContainer

def start_game_container(game, user):
    game_container_model = None
    images = game.images.all()
    if images:
        # Todo get the latest image
        game_image = images[0]
        game_container_name = secrets.token_hex(16)
        client = docker.from_env()
        if client:
            # Todo network name hardcoded
            # Todo change ports
            try:
                game_container = client.containers.run("{}:{}".format(game_image.name, game_image.version),
                        detach=True, name=game_container_name, network="gamestreaming_net")
                game_container_model = GameContainer(id=game_container.id, name=game_container_name,
                        image=game_image, is_in_use=True, user=user)
            except:
                try:
                    container = client.containers.get(game_container_name)
                    if container:
                        container.remove()
                except:
                    pass
            finally:
                client.close()
    
    return game_container_model
            

