from PIL import Image
import numpy as np

class ImageProcessor: 
    def __init__(self, ascii_chars=" ./*&#@"):
        self.ascii_chars = ascii_chars

    def __str__(self):
        print(self.im.format, self.im.size, self.im.mode)
        self.img.show()

    def open_img(self, image_path):
        self.img = Image.open(image_path)
        
    def assign_ascii(self, pixel_value):
        # normalize value of pixel to level 0 - 6 for easier ascii conversion
        normalized_value = float(pixel_value - self.min_pixel) / float(self.max_pixel - self.min_pixel) * (len(self.ascii_chars) - 1)
        return int(round(normalized_value))

    def image_to_ascii(self, image_path, width=100):
        self.img = Image.open(image_path)
        self.img = self.img.convert("L")
        aspect_ratio = self.img.height / self.img.width
        height = int(width * aspect_ratio)
        self.img = self.img.resize((width, height))
        pixels = np.array(self.img)

        # find min and max light value for mapping
        self.min_pixel = pixels.min()
        self.max_pixel = pixels.max()
        
        # start empty ascii_str
        ascii_str = ''
        for row in pixels:
            for pixel_value in row:
                ascii_str += self.ascii_chars[self.assign_ascii(pixel_value)]
            ascii_str += '\n'
            
        return ascii_str
    



