import os

path = r'c:\anti\sterlingVM\src\app\dashboard\config\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add META_AD_ACCOUNT_ID to the UI
insertion = '''                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Meta Ad Account ID</label>
                    <input type="text" value={configValues.META_AD_ACCOUNT_ID || ''} onChange={(e) => handleConfigChange('META_AD_ACCOUNT_ID', e.target.value)} placeholder="e.g. 1581126706893474" className="w-full bg-gray-50 dark:bg-black/50 border border-gray-200 dark:border-white/10 py-2.5 px-4 rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:border-blue-600 transition-all duration-300 font-mono" />
                  </div>
                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Permanent Access Token'''

content = content.replace('''                  <div>
                    <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Permanent Access Token''', insertion)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
