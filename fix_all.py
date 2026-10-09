import os
import re

dir_path = r'c:\anti\sterlingVM\src'

for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts') or f.endswith('.css'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            # Replace colors
            new_content = content.replace('red-600', 'purple-600')
            new_content = new_content.replace('indigo-500', 'purple-500')
            
            # Replace logo images
            new_content = re.sub(
                r'<img[^>]*src=\"/text_logo[^>]*>', 
                r'<div className="text-xl font-black tracking-widest text-black dark:text-white italic">STERLING<span className="text-purple-600">AI</span></div>', 
                new_content
            )
            
            # Catch any lingering Mahindra
            new_content = new_content.replace('Mahindra', 'Sterling')
            new_content = new_content.replace('mahindra', 'sterling')
            new_content = new_content.replace('MAHINDRA', 'STERLING')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
