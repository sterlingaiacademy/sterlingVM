import os
import re

dir_path = r'c:\anti\sterlingVM\src'

replacements = {
    'XUV700': 'AI Masterclass',
    'Vehicle Model': 'Program of Interest',
    'VEHICLE': 'PROGRAM',
    'Vehicle': 'Program',
    'SHOWROOM VISITS': 'CONSULTATIONS',
    'Showroom Visits': 'Consultations',
    'Showroom': 'Office',
    'SERVICE LEADS': 'SUPPORT QUERIES',
    'Service Leads': 'Support Queries',
    'test drive': 'demo',
    'Test Drive': 'Demo',
    'TEST DRIVE': 'DEMO',
    'mahindra': 'sterling',
    'Mahindra': 'Sterling'
}

for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            new_content = content
            for k, v in replacements.items():
                new_content = new_content.replace(k, v)
                
            new_content = re.sub(r'<img[^>]*src=\"/logo[^>]*>', r'<div className=\"text-2xl font-black tracking-widest text-white italic\">STERLING<span className=\"text-indigo-500\">AI</span></div>', new_content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
