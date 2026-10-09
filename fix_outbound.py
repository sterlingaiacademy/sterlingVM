import os

path = r'c:\anti\sterlingVM\src\app\dashboard\outbound\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Scorpio', 'Data Science Bootcamp')
content = content.replace('Follow up on demo enquiry', 'Follow up on enrollment enquiry')
content = content.replace('Service Reminder for 10 AM tomorrow', 'Reminder for consultation at 10 AM tomorrow')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
