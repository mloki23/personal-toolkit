import qrcode
from PIL import Image

def generate_qr_code(data, filename):
    """
    Generates a QR code from the given data and saves it to a file.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def read_qr_code(filename):
    """
    Reads a QR code from an image file and returns the decoded data.
    """
    try:
        from pyzbar.pyzbar import decode
    except ImportError:
        print("pyzbar not found. Please install it: pip install pyzbar")
        return None
    
    img = Image.open(filename)
    decoded_objects = decode(img)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    return None