def bin_to_dec(b):
    return int(b, 2)

def dec_to_bin(d):
    return bin(d)[2:]

def dec_to_hex(d):
    return hex(d)[2:].upper()

def hex_to_dec(h):
    return int(h, 16)

def ascii_to_bin(text):
    return ' '.join(format(ord(c), '08b') for c in text)
