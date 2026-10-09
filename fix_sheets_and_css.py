import os

dir_path = r'c:\anti\sterlingVM\src'
old_sheet = '1EuYUHCElFWq6AgsA-FWFGfnRCxQTOdKG_73725C0fXg'
new_sheet = '1lnhhffZuBuJKiMOaKcvnJ-aCA2p_22D9nC8GZ_hg5wc'

for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith(('.tsx', '.ts', '.css', '.bak')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            new_content = content
            new_content = new_content.replace(old_sheet, new_sheet)
            
            if f.endswith('.css'):
                new_content = new_content.replace('--color-purple-600: #e31837;', '--color-purple-600: #9333ea;')
                new_content = new_content.replace('--color-purple-600-dark: #b3122b;', '--color-purple-600-dark: #7e22ce;')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
