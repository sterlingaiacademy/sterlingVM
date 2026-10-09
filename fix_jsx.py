import os

path = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("className=	ext-[10px]", "className={	ext-[10px]")
content = content.replace("'text-gray-400'}>", "'text-gray-400'}}>")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
