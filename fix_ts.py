import os
path = r'c:\anti\sterlingVM\src\components\UpcomingEventsBoard.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('export function UpcomingEventsBoard({ logs }: { logs: any[] }) {', 'export function UpcomingEventsBoard({ data: logs }: { data: any[] }) {')
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
