import colorsys

def f(r, g, b):
    hsv = colorsys.rgb_to_hsv(r, g, b)
    print(hsv)
    
f(255, 255, 255)
