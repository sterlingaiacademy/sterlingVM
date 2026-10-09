import os
import re

path = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the function signature and add the text class logic
content = re.sub(
    r'function StatCard\(\{ title, value, icon: Icon, trend, isGood = false, delay = "0" \}: any\) \{',
    r'function StatCard({ title, value, icon: Icon, trend, isGood = false, delay = "0" }: any) {\n  const valStr = String(value);\n  const textClass = valStr.length > 15 ? "text-lg leading-tight" : valStr.length > 8 ? "text-2xl" : "text-4xl tracking-tighter";',
    content
)

# Replace the text-4xl class
content = re.sub(
    r'<div className="text-4xl font-black tracking-tighter mb-2 text-gray-900 dark:text-white relative z-10">',
    r'<div className={ont-black mb-2 text-gray-900 dark:text-white relative z-10 }>',
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
