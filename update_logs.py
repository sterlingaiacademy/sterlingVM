import os
import re

path = r'c:\anti\sterlingVM\src\components\LogsTableClient.tsx'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Table Headers
content = content.replace('<th className="p-4 text-xs font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">Program</th>', '<th className="p-4 text-xs font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">Course / Dept</th>')
content = content.replace('<th className="p-4 text-xs font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">Service/Visit</th>', '<th className="p-4 text-xs font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">Final Response</th>')
content = content.replace('<th className="p-4 text-xs font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">Enquiry</th>', '<th className="p-4 text-xs font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">Summary</th>')

# Replace Data rows
# For Course
content = re.sub(r'\{log\[\"Program of Interest\"\] \|\| \"-\"\}', r'{log["Course"] || "-"} <div className="text-[10px] text-gray-500">{log["Dept"] || ""}</div>', content)

# For Summary
# We want log["Enquiry Summary"] instead of log["Enquiry Type"]
content = content.replace('const enquiry = log["Enquiry Type"] || "-";', 'const enquiry = log["Enquiry Summary"] || "-";')

# For Final Response (was Service/Visit)
service_block = r'''{log["Service Type"] && log["Service Type"].trim() !== "" ? (
                            <div className="capitalize font-medium text-gray-900 dark:text-white">{log["Service Type"]}</div>
                          ) : (
                            <span className="text-gray-400 dark:text-gray-500 text-xs italic">N/A</span>
                          )}'''

new_response_block = r'''{log["Final Response"] && log["Final Response"].trim() !== "" ? (
                            <div className="capitalize font-medium text-gray-900 dark:text-white">{log["Final Response"]}</div>
                          ) : (
                            <span className="text-gray-400 dark:text-gray-500 text-xs italic">N/A</span>
                          )}'''
                          
content = content.replace(service_block, new_response_block)

# And in filtering logic
content = content.replace('log["Program of Interest"]', 'log["Course"]')
content = content.replace('log["Enquiry Type"]', 'log["Enquiry Summary"]')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
