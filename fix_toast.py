import os

path = r'c:\anti\sterlingVM\src\app\dashboard\campaigns\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("toast.type === 'error' ? 'bg-purple-600 border-red-700 text-white' :", "toast.type === 'error' ? 'bg-red-600 border-red-700 text-white' :")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
