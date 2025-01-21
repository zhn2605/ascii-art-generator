from PIL import Image
import numpy as np

class ImageProcessor: 
    def __init__(self, ascii_chars=" ./*&#@"):
        self.ascii_chars = ascii_chars

    def __str__(self):
        print(self.im.format, self.im.size, self.im.mode)
        self.im.show()
    
    # experiment
    def pixel_brightness(self):
        self.

    def image_to_ascii(self, image_path, width=100):
        self.img = Image.open(image_path)
        self.img = self.img.convert("L")
        aspect_ratio = self.img.height / self.img.width
        height = int(width * aspect_ratio)
        self.img = self.img.resize((width, height))
        pixels = np.array(self.img)
        
        ascii_str = ''
        for row in pixels:
            for pixel in row:
                pixel_value = self.img.getpixel((row, pixel))
                ascii_str += self.ascii_chars[self.assign_ascii(pixel_value)]
            ascii_str += '\n'
            
        return ascii_str
    
    def assign_ascii(self, pixel_value):
        


