import os
import glob

for path in glob.glob(r'c:\anti\sterlingVM\src\**\*.tsx', recursive=True):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any text-purple-600 that's inside an error state
    content = content.replace('bg-red-50 text-purple-600', 'bg-red-50 text-red-600')
    content = content.replace('bg-purple-600 border-red-700', 'bg-red-600 border-red-700')
    content = content.replace('bg-purple-600/10 text-purple-600 border-red-500', 'bg-red-500/10 text-red-500 border-red-500')
    content = content.replace('bg-purple-500', 'bg-red-500') # Wait, I don't want to replace all purple!
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
