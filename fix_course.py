import os

path = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Top Program', 'Top Course')
content = content.replace('topProgram', 'topCourse')
content = content.replace('icon={Car}', 'icon={GraduationCap}')
content = content.replace('Car, Clock', 'Car, Clock, GraduationCap')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
