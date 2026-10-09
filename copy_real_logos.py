import shutil
import os
from PIL import Image

def copy_and_crop(src_path, dest_path):
    print(f"Copying {src_path} to {dest_path}")
    shutil.copy2(src_path, dest_path)
    
    # Crop transparent padding
    img = Image.open(dest_path).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img_cropped = img.crop(bbox)
        img_cropped.save(dest_path)
        print(f"Cropped {dest_path} to {img_cropped.size}")
    else:
        print(f"Could not crop {dest_path}")

# Light mode logo (black text) -> text_logo_black.png
copy_and_crop(r'C:\Users\NIMESH\Downloads\sterling logo.png', r'c:\anti\sterlingVM\public\text_logo_black.png')

# Dark mode logo (white text) -> text_logo_white.png
copy_and_crop(r'C:\Users\NIMESH\Downloads\IMG_0242.PNG', r'c:\anti\sterlingVM\public\text_logo_white.png')

