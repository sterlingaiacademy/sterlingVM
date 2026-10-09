import os

path = r'c:\anti\sterlingVM\src\app\dashboard\config\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add IG and FB inputs
insertion = '''                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Instagram Account ID</label>
                    <input type="text" value={configValues.META_IG_ACCOUNT_ID || ''} onChange={(e) => handleConfigChange('META_IG_ACCOUNT_ID', e.target.value)} placeholder="e.g. 17841400000000000" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                  </div>
                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Facebook Page ID</label>
                    <input type="text" value={configValues.META_FB_PAGE_ID || ''} onChange={(e) => handleConfigChange('META_FB_PAGE_ID', e.target.value)} placeholder="e.g. 101234567890123" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                  </div>
                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Meta Ad Account ID'''

content = content.replace('''                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Meta Ad Account ID''', insertion)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
