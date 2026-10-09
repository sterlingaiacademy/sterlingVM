import os

path = r'c:\anti\sterlingVM\src\app\api\meta\campaign\ig-push\route.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('imageUrl.match(/^data:([A-Za-z-+\\%+);base64,(.+)$/);', r'imageUrl.match(/^data:([A-Za-z-+\\/]+);base64,(.+)$/);')
content = content.replace('imageUrl.match(/^data:([A-Za-z-+\/%+);base64,(.+)$/);', r'imageUrl.match(/^data:([A-Za-z-+\\/]+);base64,(.+)$/);')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
