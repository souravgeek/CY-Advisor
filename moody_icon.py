import base64
from PIL import Image, ImageDraw
import io
import os

def create_moody_icon():
    # Create a 64x64 image with transparent background
    img = Image.new('RGBA', (64, 64), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a magical eye (Moody's iconic feature)
    # The outer eye
    draw.ellipse((10, 10, 54, 54), fill=(70, 130, 180, 255))  # Steel blue
    
    # The iris
    draw.ellipse((20, 20, 44, 44), fill=(255, 215, 0, 255))  # Gold
    
    # The pupil
    draw.ellipse((27, 27, 37, 37), fill=(0, 0, 0, 255))
    
    # Add some magical sparkles
    draw.line((5, 5, 15, 15), fill=(255, 255, 255, 200), width=2)
    draw.line((59, 5, 49, 15), fill=(255, 255, 255, 200), width=2)
    draw.line((5, 59, 15, 49), fill=(255, 255, 255, 200), width=2)
    draw.line((59, 59, 49, 49), fill=(255, 255, 255, 200), width=2)
    
    # Save the icon
    img.save("moody_icon.ico", format="ICO")
    print("Icon created successfully!")

if __name__ == "__main__":
    create_moody_icon() 