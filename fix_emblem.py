import os

def update_logo(path, old_str, new_str):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old_str, new_str)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update Login Page
update_logo(
    r'c:\anti\sterlingVM\src\app\login\page.tsx', 
    r'<img src="/text_logo_white.png" alt="Sterling Logo" className="h-[60px] w-auto object-contain drop-shadow-xl" />', 
    r'<img src="/emblem.png" alt="Sterling Emblem" className="h-[80px] w-auto object-contain drop-shadow-xl" />'
)

# Update Landing Page
update_logo(
    r'c:\anti\sterlingVM\src\app\page.tsx', 
    r'<img src="/text_logo_white.png" alt="Sterling Logo" className="h-[45px] w-auto object-contain" />', 
    r'<img src="/emblem.png" alt="Sterling Emblem" className="h-[60px] md:h-[85px] w-auto object-contain drop-shadow-md" />'
)
