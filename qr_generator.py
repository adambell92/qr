import qrcode
import argparse

def generate_qr(data, filename="qr_code.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save image
    qr_image.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate QR Code')
    parser.add_argument('data', help='Data to encode in QR code')
    parser.add_argument('--output', '-o', help='Output file name', default='qr_code.png')
    
    args = parser.parse_args()
    generate_qr(args.data, args.output)
