import os

path = r'c:\anti\sterlingVM\src\app\dashboard\layout.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('} from "lucide-react";', ', BarChart3 } from "lucide-react";')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
