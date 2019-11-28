def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    
    if any(color not in range(0, 256) for color in rgb):
        raise ValueError
    
    return '#{:02X}{:02X}{:02X}'.format(*rgb)