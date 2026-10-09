import os

path = r'c:\anti\sterlingVM\src\app\dashboard\config\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the app id and app secret divs with facebook and instagram divs.
old_app_id = '''<div>
                  <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">App ID</label>
                  <input type="text" value={configValues.META_APP_ID || ''} onChange={(e) => handleConfigChange('META_APP_ID', e.target.value)} placeholder="e.g. 1405743091375589" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                </div>
                <div>
                  <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">App Secret</label>
                  <input type="password" value={configValues.META_APP_SECRET || ''} onChange={(e) => handleConfigChange('META_APP_SECRET', e.target.value)} placeholder="Enter App Secret" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                </div>'''

new_fields = '''<div>
                  <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Instagram Account ID</label>
                  <input type="text" value={configValues.IG_ACCOUNT_ID || ''} onChange={(e) => handleConfigChange('IG_ACCOUNT_ID', e.target.value)} placeholder="e.g. 17841400000000000" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                </div>
                <div>
                  <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Facebook Page ID</label>
                  <input type="text" value={configValues.FB_PAGE_ID || ''} onChange={(e) => handleConfigChange('FB_PAGE_ID', e.target.value)} placeholder="e.g. 101234567890123" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                </div>'''

content = content.replace(old_app_id, new_fields)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
