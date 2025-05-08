from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += chr(0)  # Delimiter to mark end of message
    data = ''.join(f'{ord(c):08b}' for c in message)
    
    if len(data) > width * height * 3:
        raise ValueError("Message is too long to encode in image.")
    
    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):  # R, G, B
                if data_index < len(data):
                    pixel[i] = pixel[i] & ~1 | int(data[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if data_index >= len(data):
                encoded.save(output_path)
                print(f"✅ Message encoded and saved to {output_path}")
                return

def decode_message(image_path):
    img = Image.open(image_path)
    data = ''
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            for i in range(3):  # R, G, B
                data += str(pixel[i] & 1)
    
    chars = [chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8)]
    message = ''.join(chars)
    message = message.split(chr(0))[0]
    print(f"🔍 Hidden Message: {message}")

# Example Usage:
# encode_message("secret_image.png", "I hacked the planet 😈", "encoded_image.png")
# decode_message("encoded_image.png")
