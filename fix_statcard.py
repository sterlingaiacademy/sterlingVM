import os

path = r'c:\anti\sterlingVM\src\app\dashboard\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_stat = '''function StatCard({ title, value, icon: Icon, trend, isGood = false, delay = "0" }: any) {
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
      
      <div className="text-4xl font-black tracking-tighter mb-2 text-gray-900 dark:text-white relative z-10">
        {value}
      </div>'''

new_stat = '''function StatCard({ title, value, icon: Icon, trend, isGood = false, delay = "0" }: any) {
  const valStr = String(value);
  const textClass = valStr.length > 15 ? "text-xl leading-tight" : valStr.length > 8 ? "text-2xl" : "text-4xl tracking-tighter";

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
      
      <div className={ont-black mb-2 text-gray-900 dark:text-white relative z-10 }>
        {value}
      </div>'''

content = content.replace(old_stat, new_stat)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
