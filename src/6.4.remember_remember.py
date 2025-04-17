from PIL import Image

def remember_remember(path):
    try:
        img = Image.open(path).convert('RGB')
        pixels = list(img.getdata())
        bits = ''.join([str(r & 1) for r, g, b in pixels])
        chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        message = ''.join(chars).split('\x00')[0]
        return message
    except Exception:
        return None
