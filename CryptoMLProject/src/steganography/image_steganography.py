from PIL import Image

def encode_image(image_path: str, message: str, output_path: str):
    """Codifica uma mensagem em uma imagem"""
    image = Image.open(image_path)
    encoded_image = image.copy()
    pixels = encoded_image.load()
    message_bits = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # Fim da mensagem
    index = 0
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            if index < len(message_bits):
                r = (r & 0xFE) | int(message_bits[index])
                index += 1
            if index < len(message_bits):
                g = (g & 0xFE) | int(message_bits[index])
                index += 1
            if index < len(message_bits):
                b = (b & 0xFE) | int(message_bits[index])
                index += 1
            pixels[x, y] = (r, g, b)
            if index >= len(message_bits):
                break
    encoded_image.save(output_path)
