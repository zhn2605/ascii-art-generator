from PIL import Image, ImageDraw, ImageFont
import os
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
    
    def save_ascii_as_image(self, ascii_str, output_path, font_size=12, padding=10):
        # add file extension if none
        if not os.path.splitext(output_path)[1]:
            output_path += '.jpg'

        # split ascii_strinto lines
        lines = ascii_str.split('\n')

        try:
            font = ImageFont.truetype("Courier")
        except OSError:
            font = ImageFont.load_default()

        sample_char = 'X'
        char_width = font.getbbox(sample_char)[2]# get right bounding box 
        char_spacing = int(char_width * .2)
        char_height = font_size

        # set size of image
        img_width = char_width * (max(len(line) for line in lines)) + (2 * padding)
        img_height = char_height * len(lines) + (2 * padding)

        ascii_img = Image.new("L", (img_width, img_height), color=0)
        draw = ImageDraw.Draw(ascii_img)
        
        # draw
        y = padding
        for line in lines:
            x = padding
            for char in line:
                draw.text((x, y), char, font=font, fill=255)
                x += char_width + char_spacing
            y += char_height

        # save image
        ascii_img.save(output_path)
        return output_path


