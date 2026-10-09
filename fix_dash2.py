import os
import re

path_dash = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path_dash, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure the UI labels reflect exactly what they want, and they pull correctly from the sheet
content = content.replace('log["Pass Out Year"] && log["Pass Out Year"].trim() !== ""', 'log["Final Response"] && log["Final Response"].trim() !== ""')
content = content.replace('log["Call Type"] && log["Call Type"].trim() !== ""', 'log["Call Type"] && log["Call Type"].toLowerCase() === "inbound"')

with open(path_dash, 'w', encoding='utf-8') as f:
    f.write(content)

path_charts = r'c:\anti\sterlingVM\src\components\DashboardCharts.tsx'
with open(path_charts, 'r', encoding='utf-8') as f:
    charts = f.read()

charts = charts.replace('const hasService = log["Call Type"] && log["Call Type"].trim() !== "" && log["Call Type"].trim() !== "-";', 'const hasService = log["Call Type"] && log["Call Type"].toLowerCase() === "inbound";')
charts = charts.replace('const hasVisit = log["Pass Out Year"] && log["Pass Out Year"].trim() !== "" && log["Pass Out Year"].trim() !== "-";', 'const hasVisit = log["Final Response"] && log["Final Response"].trim() !== "" && log["Final Response"].trim() !== "-";')

with open(path_charts, 'w', encoding='utf-8') as f:
    f.write(charts)
