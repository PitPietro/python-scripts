import os
from PIL import ImageGrab
from datetime import datetime


if __name__ == '__main__':
    image = ImageGrab.grab()
    now = datetime.now()
    extension = '.png'
    name = 'screen' + now.strftime('_%d-%m-%y_%H-%M-%S') + extension
    # os.environ['USER'] --> pit VS os.environ['HOME'] --> /home/pit
    home = os.environ['HOME']
    dest = '/Desktop/'
    final_path = home + dest
    image.save(final_path)
