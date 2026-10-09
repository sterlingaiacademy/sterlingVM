import os

page_path = r'c:\anti\sterlingVM\src\app\page.tsx'
with open(page_path, 'r', encoding='utf-8') as f:
    page_content = f.read()

# Fix the two logos
bad_logos = '''<img src="/emblem.png" alt="Sterling Emblem" className="h-[60px] md:h-[85px] w-auto object-contain drop-shadow-md" />
          <img src="/emblem.png" alt="Sterling Emblem" className="h-[60px] md:h-[85px] w-auto object-contain drop-shadow-md" />'''

good_logo = '''<img src="/emblem.png" alt="Sterling Emblem" className="h-[60px] md:h-[85px] w-auto object-contain drop-shadow-md" />'''

page_content = page_content.replace(bad_logos, good_logo)
page_content = page_content.replace('dealership.', 'institute.')

with open(page_path, 'w', encoding='utf-8') as f:
    f.write(page_content)
