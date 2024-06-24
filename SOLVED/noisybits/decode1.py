from PIL import Image
import zipfile
import os

def bmp_to_bits(image_path):
    """Converts a BMP image to a list of bits where black pixels are 0 and white pixels are 1."""
    img = Image.open(image_path)
    img = img.convert('1')  # Convert image to 1-bit pixels (black and white)
    
    # Get pixel data as bytes
    byte_data = img.tobytes()
    
    # Convert bytes to bits
    bits = []
    for byte in byte_data:
        # Convert each byte to its binary representation
        bits.extend([(byte >> bit) & 1 for bit in range(7, -1, -1)])
    
    return bits

def bits_to_bytes(bits):
    """Converts a list of bits to bytes."""
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        byte_array.append(byte)
    return bytes(byte_array)

def write_zip_from_bytes(byte_array, zip_file_path):
    """Writes the byte array to a ZIP file."""
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(byte_array)

def bmp_to_zip(image_path, zip_file_path):
    """Converts a BMP image to a ZIP file based on the bit pattern."""
    # Convert BMP to bits
    bits = bmp_to_bits(image_path)
    
    # Convert bits to bytes
    byte_array = bits_to_bytes(bits)
    
    # Write bytes to ZIP file
    write_zip_from_bytes(byte_array, zip_file_path)

# Example usage:
image_path = 'bits.bmp'  # Path to your BMP image representing bits
zip_file_path = 'output.zip'  # Path to save the ZIP file
bmp_to_zip(image_path, zip_file_path)
