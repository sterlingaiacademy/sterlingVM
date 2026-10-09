import os

path = r'c:\anti\sterlingVM\src\components\UpcomingEventsBoard.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

filter_block = '''  } else if (selectedDate === "yesterday") {
    displayEvents = allEvents.filter(e => e.date === yesterday);
  } else if (selectedDate === "past") {
    displayEvents = allEvents.filter(e => e.date < yesterday);
  } else if (selectedDate === "all") {'''
new_filter_block = '''  } else if (selectedDate === "yesterday") {
    displayEvents = allEvents.filter(e => e.date === yesterday);
  } else if (selectedDate === "all") {'''

button_block = '''          <button 
            onClick={() => setSelectedDate("yesterday")}
            className={px-5 py-2 text-[10px] font-extrabold uppercase tracking-widest rounded-lg transition-all duration-300 }
          >
            Yesterday
          </button>
          <button 
            onClick={() => setSelectedDate("past")}
            className={px-5 py-2 text-[10px] font-extrabold uppercase tracking-widest rounded-lg transition-all duration-300 }
          >
            Past
          </button>'''
new_button_block = '''          <button 
            onClick={() => setSelectedDate("yesterday")}
            className={px-5 py-2 text-[10px] font-extrabold uppercase tracking-widest rounded-lg transition-all duration-300 }
          >
            Yesterday
          </button>'''

content = content.replace(filter_block, new_filter_block)
content = content.replace(button_block, new_button_block)
content = content.replace('selectedDate !== "past" && ', '')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
