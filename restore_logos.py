import os

dir_path = r'c:\anti\sterlingVM\src'

old_logo = r'<div className="text-xl font-black tracking-widest text-black dark:text-white italic">STERLING<span className="text-purple-600">AI</span></div>'
new_logo_layout = r'<img src="/text_logo_white.png" alt="Sterling Text" className="h-[40px] w-auto object-contain shrink-0" />'

old_login_logo = r'<div className="text-2xl font-black tracking-widest text-white italic">STERLING<span className="text-purple-600">AI</span></div>'
new_login_logo = r'<img src="/text_logo_white.png" alt="Sterling Logo" className="h-[60px] w-auto object-contain drop-shadow-xl" />'

for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = content.replace(old_logo, new_logo_layout)
            new_content = new_content.replace(old_login_logo, new_login_logo)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
