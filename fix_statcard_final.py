import base64
import os
import re

path = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

statcard_code = '''function StatCard({ title, value, icon: Icon, trend, isGood = false, delay = "0" }: any) {
  const valStr = String(value).trim();
  const isVeryLong = valStr.length > 13;
  const isLong = valStr.length > 7;

  return (
    <div 
      className="group relative bg-white dark:bg-[#050505] border border-gray-100 dark:border-white/5 p-6 rounded-3xl hover:border-purple-600/30 dark:hover:border-purple-600/50 hover:shadow-2xl hover:-translate-y-2 transition-all duration-500 overflow-hidden cursor-default"
      style={{ animationDelay: ${delay}ms }}
    >
      <div className="absolute inset-0 bg-gradient-to-br from-purple-600/0 to-purple-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
      
      <div className="flex justify-between items-start mb-6 relative z-10">
        <h3 className="text-[10px] font-extrabold uppercase tracking-widest text-gray-400 group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-colors">{title}</h3>
        <div className="w-8 h-8 rounded-full bg-gray-50 dark:bg-white/5 flex items-center justify-center group-hover:bg-purple-600/10 group-hover:scale-110 transition-all duration-300">
          <Icon className="w-4 h-4 text-gray-400 group-hover:text-purple-600 transition-colors" />
        </div>
      </div>
      
      <div 
        className="font-black mb-2 text-gray-900 dark:text-white relative z-10"
        style={{
          fontSize: isVeryLong ? '1.5rem' : isLong ? '1.75rem' : '2.5rem',
          lineHeight: isVeryLong ? '1.2' : '1',
          letterSpacing: '-0.05em'
        }}
      >
        {value}
      </div>
      
      <div className={"text-[10px] font-bold uppercase tracking-widest relative z-10 flex items-center gap-1.5 " + (isGood ? "text-green-500" : "text-gray-400")}>
        {trend}
      </div>
    </div>
  );
}'''

content = re.sub(r'function StatCard\(\{.*?^\}', statcard_code, content, flags=re.MULTILINE | re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
