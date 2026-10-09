import os

path = r'c:\anti\sterlingVM\src\app\dashboard\campaigns\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('https://sterling.com/test-drive', 'https://sterlingaiacademy.com/enroll')
content = content.replace('#sterling #SUV #Explore', '#sterlingAI #Education #Future')
content = content.replace('sterling PPS Motors', 'Sterling AI Academy')
content = content.replace('sterling_pps', 'sterling_ai_academy')
content = content.replace('Book Demo', 'Enroll Now')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
