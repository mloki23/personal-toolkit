from PIL import Image

def resize_image(input_path, output_path, width, height):
    """
    Resizes an image to the specified width and height.
    """
    with Image.open(input_path) as img:
        img = img.resize((width, height))
        img.save(output_path)

def convert_image(input_path, output_path, format):
    """
    Converts an image to the specified format.
    """
    with Image.open(input_path) as img:
        img.save(output_path, format=format)