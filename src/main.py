from image import ImageProcessor

imageProcessor = ImageProcessor()
logo = imageProcessor.image_to_ascii("../images/AAC_logo.jpg", 100)
print(('-' * 150 + '\n') * 2)
print(logo)
print(('-' * 150 + '\n') * 2)

while True:
    # Get user filename
    filename = input("Enter your file name: ")
    width = input("Enter size of ascii art (in pixels): ")

    # Validate width input
    while not width.isdigit():
        width = input("Size of ascii art must be a number: ")

    width = int(width)

    processd_txt = imageProcessor.image_to_ascii(filename, width)
    print(processd_txt)
    
    save_img = input("Would you like to save this image? (y/n): ")[0].lower()

    while save_img != 'y' and save_img != 'n':
        save_img = input("Invalid choice. Please write 'y' for yes and 'n' for no: ")

    if save_img == 'y':
        output_path = input("Enter an output path (Recommended -> ../images/<image name>): ")
        imageProcessor.save_ascii_as_image(processd_txt, output_path)
    
    stop = input("Would you like to convert another file? (y/n): ")[0].lower()

    if stop != 'y':
        break

print("Goodbye!")