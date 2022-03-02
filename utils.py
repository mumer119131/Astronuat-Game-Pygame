from pygame.image import load
from pathlib import Path

def load_sprite(name, withAlpha = True):
    filename = Path(__file__).parent / Path("assets/sprites/"+ name + ".png")
    print(filename)
    sprite = load(filename.resolve())
    
    if withAlpha:
        return sprite.convert_alpha()

    return sprite.convert()    