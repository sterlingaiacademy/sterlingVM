import os

path = r'c:\anti\sterlingVM\src\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_logo = r'<div className="text-2xl font-black tracking-widest text-white italic">STERLING<span className="text-purple-500">AI</span></div>'
new_logo = r'<img src="/text_logo_white.png" alt="Sterling Logo" className="h-[45px] w-auto object-contain" />'

content = content.replace(old_logo, new_logo)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
