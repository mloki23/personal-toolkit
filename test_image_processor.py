import os
import unittest
from PIL import Image
from personal_toolkit_image_processor import resize_image, convert_image

class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        self.test_image_dir = "test_images"
        os.makedirs(self.test_image_dir, exist_ok=True)
        self.input_image_path = os.path.join(self.test_image_dir, "test_image.png")
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(self.input_image_path)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_image_dir)

    def test_resize_image(self):
        output_path = os.path.join(self.test_image_dir, "resized_image.png")
        resize_image(self.input_image_path, output_path, 50, 50)
        self.assertTrue(os.path.exists(output_path))
        with Image.open(output_path) as img:
            self.assertEqual(img.size, (50, 50))

    def test_convert_image(self):
        output_path = os.path.join(self.test_image_dir, "converted_image.jpg")
        convert_image(self.input_image_path, output_path, "JPEG")
        self.assertTrue(os.path.exists(output_path))
        with Image.open(output_path) as img:
            self.assertEqual(img.format, "JPEG")