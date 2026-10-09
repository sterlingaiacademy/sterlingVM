import os

dir_path = r'c:\anti\sterlingVM\src'

for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts') or f.endswith('.css'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            # Replace colors
            new_content = content.replace('sterling-red', 'purple-600')
            new_content = new_content.replace('mahindra-red', 'purple-600')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
