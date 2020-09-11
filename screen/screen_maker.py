from PIL import ImageGrab


if __name__ == '__main__':
    image = ImageGrab.grab()
    image.save('test.png')
