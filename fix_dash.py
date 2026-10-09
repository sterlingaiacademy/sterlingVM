import os

path_dash = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path_dash, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('log["Visit Day"]', 'log["Pass Out Year"]')
content = content.replace('log["Service Type"]', 'log["Call Type"]')
content = content.replace('log["Program of Interest"]', 'log["Course"]')
content = content.replace('if (vehicle.toLowerCase().includes("xuv seven")) vehicle = "AI Masterclass";', '')
content = content.replace('if (vehicle.toLowerCase().includes("xuv three")) vehicle = "XUV300";', '')

with open(path_dash, 'w', encoding='utf-8') as f:
    f.write(content)

path_charts = r'c:\anti\sterlingVM\src\components\DashboardCharts.tsx'
with open(path_charts, 'r', encoding='utf-8') as f:
    charts = f.read()

charts = charts.replace("['#E21836', '#FF9800', '#4CAF50', '#2196F3', '#9C27B0']", "['#9333ea', '#c084fc', '#d8b4fe', '#6b21a8', '#3b0764']")
charts = charts.replace('log["Program of Interest"]', 'log["Course"]')
charts = charts.replace('if (v.toLowerCase().includes("xuv seven")) v = "AI Masterclass";', '')
charts = charts.replace('if (v.toLowerCase().includes("xuv three")) v = "XUV300";', '')

charts = charts.replace('log["Service Type"]', 'log["Call Type"]')
charts = charts.replace('log["Visit Day"]', 'log["Pass Out Year"]')

# Fix bar chart colors
charts = charts.replace('fill="#E21836"', 'fill="#9333ea"')
charts = charts.replace('fill="#4CAF50"', 'fill="#c084fc"')
charts = charts.replace('fill="#555"', 'fill="#6b21a8"')
charts = charts.replace('Office Booking', 'Outbound')
charts = charts.replace('Service Lead', 'Inbound')

with open(path_charts, 'w', encoding='utf-8') as f:
    f.write(charts)
