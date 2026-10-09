import os

dir_path = r'c:\anti\sterlingVM\src'

for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            # Remove literal backslashes from className
            new_content = content.replace(r'className=\"', 'className="')
            new_content = new_content.replace(r'\">STERLING<span', '">STERLING<span')
            new_content = new_content.replace(r'\">AI</span></div>', '">AI</span></div>')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
