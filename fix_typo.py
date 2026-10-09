import os

path = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('d\ms }}', '\\ms\ }}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
