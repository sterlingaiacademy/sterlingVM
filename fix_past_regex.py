import os
import re

path = r'c:\anti\sterlingVM\src\components\UpcomingEventsBoard.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Past button block
content = re.sub(r'<button\s*onClick=\{\(\) => setSelectedDate\("past"\)\}.*?</button>', '', content, flags=re.DOTALL)

# Remove the Past filter logic
content = re.sub(r'\} else if \(selectedDate === "past"\) \{\s*displayEvents = allEvents\.filter\(e => e\.date < yesterday\);\s*', '', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
