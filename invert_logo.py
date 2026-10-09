from PIL import Image

def invert_white_to_black(img_path):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # item is (R, G, B, A)
        if item[3] > 0: # If pixel is not fully transparent
            # Since it's white text, we want to make it black text
            new_data.append((0, 0, 0, item[3]))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(img_path)
    print(f"Inverted {img_path}")

invert_white_to_black(r'c:\anti\sterlingVM\public\text_logo_black.png')
