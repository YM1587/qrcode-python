import qrcode  # Import the actual library, not your script
from PIL import Image

def generate_qr_code(data, filename):

    #create a qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    #Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    #generate the qr code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Get input from the user
data = input("Enter the text or URL to encode: ")
filename = input("Enter the filename (e.g., qrcode.png): ")

generate_qr_code(data, filename)
