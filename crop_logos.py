from PIL import Image

def crop_transparent(img_path):
    img = Image.open(img_path).convert("RGBA")
    
    # Get the bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        img_cropped = img.crop(bbox)
        img_cropped.save(img_path)
        print(f"Cropped {img_path} to {img_cropped.size}")
    else:
        print(f"Could not crop {img_path}")

crop_transparent(r'c:\anti\sterlingVM\public\text_logo_white.png')
crop_transparent(r'c:\anti\sterlingVM\public\text_logo_black.png')
