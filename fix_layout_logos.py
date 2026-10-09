import os

path = r'c:\anti\sterlingVM\src\app\dashboard\layout.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_logo = r'<img src="/text_logo_white.png" alt="Sterling Text" className="h-[40px] w-auto object-contain shrink-0" />'
new_logo = r'<img src="/text_logo_black.png" alt="Sterling Text" className="h-[40px] w-auto object-contain dark:hidden opacity-90 shrink-0" />' + '\n' + r'                <img src="/text_logo_white.png" alt="Sterling Text" className="h-[40px] w-auto object-contain hidden dark:block opacity-90 shrink-0" />'

content = content.replace(old_logo, new_logo)

old_logo2 = r'<img src="/text_logo_white.png" alt="Sterling Text" className="h-[40px] w-auto object-contain shrink-0" />'
new_logo2 = r'<img src="/text_logo_black.png" alt="Sterling Text" className="h-[32px] w-auto object-contain dark:hidden opacity-90" />' + '\n' + r'                <img src="/text_logo_white.png" alt="Sterling Text" className="h-[32px] w-auto object-contain hidden dark:block opacity-90" />'
# Wait, the mobile one might have h-[32px]? The previous python script replaced everything with h-[40px]. Let's just do it cleanly.

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
