import os

path = r'c:\anti\sterlingVM\src\app\dashboard\layout.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('h-[40px] w-auto object-contain', 'w-[160px] h-auto max-h-[56px] object-contain')
content = content.replace('h-[32px] w-auto object-contain', 'w-[120px] h-auto max-h-[40px] object-contain')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
