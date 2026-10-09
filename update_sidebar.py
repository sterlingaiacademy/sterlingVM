import os

path = r'c:\anti\sterlingVM\src\app\dashboard\layout.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will add the BarChart3 import and the nav item
content = content.replace('LayoutDashboard, Settings, PhoneOutgoing, ScrollText, Megaphone', 'LayoutDashboard, Settings, PhoneOutgoing, ScrollText, Megaphone, BarChart3')
content = content.replace('{ label: "Meta Campaigns", href: "/dashboard/campaigns", icon: Megaphone },', '{ label: "Meta Campaigns", href: "/dashboard/campaigns", icon: Megaphone },\n    { label: "Meta Analytics", href: "/dashboard/analytics", icon: BarChart3 },')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
