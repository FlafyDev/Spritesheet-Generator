from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import numpy as np


class Spritesheet:
    def __init__(self):
        self.sprite_paths = []
        self.sprites = []

    def add_sprites(self, sprite_paths):
        for sprite_path in sprite_paths:
            loaded_sprite = Image.open(sprite_path)
            self.sprites.append(loaded_sprite)

    def generate(self):
        # Get size
        slot_size = np.array([0, 0])

        for sprite in self.sprites:
            if slot_size[0] < sprite.size[0]:
                slot_size[0] = sprite.size[0]

            if slot_size[1] < sprite.size[1]:
                slot_size[1] = sprite.size[1]

        print("Slot size:", slot_size)

        spritesheet_size = slot_size.copy()
        spritesheet_size[0] *= len(self.sprites)

        # Create image
        spritesheet_image = Image.new("RGBA", spritesheet_size.tolist(), (0, 0, 0, 0))

        # Paste sprites
        for index, sprite in enumerate(self.sprites):
            sprite_size = np.array(sprite.size)
            print("printed", index)
            position = slot_size[0] * index, 0
            spritesheet_image.paste(sprite, (-sprite_size / 2 + slot_size / 2 + position).astype(int).tolist())

        spritesheet_image.show()


def choose_images():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    return askopenfilename(multiple=True, filetypes=("images {.BMP .EPS .GIF .ICNS .ICO .IM .JPEG .MSP .PCX .PNG "
                                                     ".PPM .SGI .TIFF .WebP}", ("all files", "*.*")))


def main():
    images = choose_images()

    spritesheet = Spritesheet()
    spritesheet.add_sprites(images)
    spritesheet.generate()


if __name__ == "__main__":
    main()
