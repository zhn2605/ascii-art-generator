from image import ImageProcessor

imageProcessor = ImageProcessor()
logo = imageProcessor.image_to_ascii("../images/AAC_logo.jpg", 100)
print(('-' * 150 + '\n') * 2)
print(logo)
print(('-' * 150 + '\n') * 2)


# Get user filename
filename = input("Enter your file name: ")
width = input("Enter size of ascii art (in pixels): ")

# Validate width input
while not width.isdigit():
    width = input("Size of ascii art must be a number: ")

width = int(width)

processd_image = imageProcessor.image_to_ascii(filename, width)
print(processd_image)