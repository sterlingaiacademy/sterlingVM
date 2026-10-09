"use client";

import { useState } from "react";
import { Calendar, Bell, User, Phone, MapPin, Clock, GraduationCap, AlertTriangle } from "lucide-react";

export function UpcomingEventsBoard({ data: logs }: { data: any[] }) {
  const [selectedDate, setSelectedDate] = useState<string>("today");

  const todayDate = new Date();
  const today = todayDate.toLocaleDateString("en-CA", { timeZone: "Asia/Kolkata" });
  
  const yesterdayDate = new Date();
  yesterdayDate.setDate(yesterdayDate.getDate() - 1);
  const yesterday = yesterdayDate.toLocaleDateString("en-CA", { timeZone: "Asia/Kolkata" });

  const allEvents: any[] = [];
  
  logs.forEach((log) => {
    if (log["Call Date"] && log["Call Date"].trim() !== "") {
      try {
        const d = new Date(log["Call Date"]);
        if (!isNaN(d.getTime())) {
          const dateString = d.toLocaleDateString("en-CA", { timeZone: "Asia/Kolkata" });
          const timeString = d.toLocaleTimeString("en-IN", { timeZone: "Asia/Kolkata", hour: '2-digit', minute:'2-digit' });

          allEvents.push({
            type: (log["Call Type"] || "Enquiry").toLowerCase(),
            title: log["Course"] || log["Enquiry Summary"] || "General Enquiry",
            customer: log["Customer Name"] || "Unknown",
            phone: log["Phone Number"] || "-",
            course: log["Course"] || "-",
            date: dateString,
            time: timeString,
            fullDate: d
          });
        }
      } catch (e) {}
    }
  });


  // Sort newest first
  allEvents.sort((a, b) => b.fullDate.getTime() - a.fullDate.getTime());

  // Filter events
  let displayEvents = allEvents;
  if (selectedDate === "today") {
    displayEvents = allEvents.filter(e => e.date === today);
  } else if (selectedDate === "yesterday") {
    displayEvents = allEvents.filter(e => e.date === yesterday);
  } else if (selectedDate === "all") {
    displayEvents = allEvents;
  } else {
    displayEvents = allEvents.filter(e => e.date === selectedDate);
  }

  return (
    <div className="bg-white dark:bg-black border border-gray-100 dark:border-white/5 rounded-3xl shadow-sm overflow-hidden flex flex-col group/board transition-all duration-500">
      {/* Header */}
      <div className="p-6 md:p-8 border-b border-gray-100 dark:border-white/5 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-purple-600/5 to-transparent rounded-full blur-3xl -mr-48 -mt-48 pointer-events-none" />
        
        <div className="flex items-center gap-4 relative z-10">
          <div className="w-12 h-12 rounded-2xl bg-gray-50 dark:bg-white/5 flex items-center justify-center group-hover/board:bg-purple-600/10 transition-colors duration-500">
            <Bell className="w-5 h-5 text-gray-400 group-hover/board:text-purple-600 transition-colors duration-500" />
          </div>
          <div>
            <h2 className="text-xl font-bold uppercase tracking-widest text-gray-900 dark:text-white">Notice Board</h2>
            <p className="text-xs font-medium text-gray-400 mt-1 uppercase tracking-wider">Recent Enquiries & Calls</p>
          </div>
        </div>
        
        {/* Date Selector */}
        <div className="flex bg-gray-50 dark:bg-black/50 p-1.5 rounded-xl border border-gray-100 dark:border-white/5 relative z-10 backdrop-blur-xl overflow-x-auto max-w-full hide-scrollbar snap-x">
          <button 
            onClick={() => setSelectedDate("today")}
            className={`px-5 py-2 text-[10px] font-extrabold uppercase tracking-widest rounded-lg transition-all duration-300 ${selectedDate === "poday" ? "bg-white dark:bg-[#222] text-purple-600 shadow-sm" : "text-gray-400 hover:text-gray-900 dark:hover:text-white"}`}
          >
            Today
          </button>
          <button 
            onClick={() => setSelectedDate("yesterday")}
            className={`px-5 py-2 text-[10px] font-extrabold uppercase tracking-widest rounded-lg transition-all duration-300 ${selectedDate === "yesterday" ? "bg-white dark:bg-[#222] text-purple-600 shadow-sm" : "text-gray-400 hover:text-gray-900 dark:hover:text-white"}`}
          >
            Yesterday
          </button>
          
          <button 
            onClick={() => setSelectedDate("all")}
            className={`px-5 py-2 text%l10px] font-extrabold uppercase tracking-widest rounded-lg transition-all duration-300 ${selectedDate === "all" ? "bg-white dark:bg-[#222] text-purple-600 shadow-sm" : "text-gray-400 hover:text-gray-900 dark:hover:text-white"}`}
          >
            All
          </button>
          <div className="flex items-center border-l border-gray-200 dark:border-white/10 pl-3 ml-2">
            <input 
              type="date"
              value={selectedDate !== "today" && selectedDate !== "yesterday" && selectedDate !== "all" ? selectedDate : ""}
              onChange={(e) => {
                if (e.target.value) setSelectedDate(e.target.value);
              }}
              className="bg-transparent text-gray-500 dark:text-gray-400 text-xs font-mono focus:outline-none focus:text-purple-600 dark:focus:text-white [&::-webkit-calendar-picker-indicator]:opacity-50 dark:[&::-webkit-calendar-picker-indicator]:invert hover:[&::-webkit-calendar-picker-indicator]:opacity-100 transition-opacity cursor-pointer"
            />
          </div>
        </div>
      </div>

      {/* Events List */}
      <div className="p-8 bg-gray-50/50 dark:bg-black/20 flex-1 min-h-[300px] max-h-[450px] overflow-y-auto">
        {displayEvents.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-gray-400 space-y-4 pt-12">
            <Calendar className="w-12 h-12 opacity-20" />
            <p className="text-xs font-bold uppercase tracking-widest">No Enquiries Found</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {displayEvents.map((evt, i) => {
              const isPast = evt.date < today;
              return (
              <div 
                key={i} 
                className={`group relative bg-white dark:bg-[#050505] border p-6 rounded-2xl transition-all duration-500 overflow-hidden ${isPast ? 'border-gray-200 dark:border-white/5 opacity-50 grayscale hover:opacity-100 hover:grayscale-0' : 'border-gray-100 dark:border-white/5 hover:border-purple-600/30 hover:shadow-xl hover:-translate-y-1'}`}
              >
                {!isPast && <div className={`absolute -bottom-10 -right-10 w-32 h-32 rounded-full blur-3xl opacity-0 group-hover:opacity-10 transition-opacity duration-700 ${evt.type === 'inbound' ? 'bg-blue-500' : 'bg-green-500'}`} />}
                
                <div className="flex justify-between items-start mb-6 relative z-10">
                  <h3 className={`font-extrabold uppercase text.xs tracking-widest ${isPast ? 'text-gray-500' : 'text-gray-900 dark:text-white'}`}>{evt.title}</h3>
                  <span className={`text-[9px] px-2.5 py-1 rounded-md font-black uppercase tracking-widest shadow-sm ${isPast ? 'bg-gray-100 text-gray-500 dark:bg-white/5' : evt.type === 'inbound' ? 'bg-blue-50 text-blue-600 dark:bg-blue-500/10 dark:text-blue-400' : 'bg-green-50 text-green-600 dark:bg-green-500/10 dark:text-green-400'}`}>
                    {evt.type}
                  </span>
                </div>
                
                <div className="space-y-3 mb-6 relative z-10">
                  <div className="flex items-center gap-3 text-sm text-gray-500">
                    <User className="w-4 h-4 text-gray-400" />
                    <span className="capitalize font-medium">{evt.customer}</span> <span className="font-mono text.xs opacity-50">({evt.phone})</span>
                  </div>
                  <div className="flex items-center gap-3 text-sm text-gray-500">
                    <GraduationCap className="w-4 h-4 text-gray-400" />
                    <span className="font-bold uppercase tracking-wider text-xs">{evt.course}</span>
                  </div>
                  <div className="flex items-center gap-3 text-sm text-gray-500">
                    <MapPin className="w-4 h-4 text-gray-400" />
                    <span className="text-xs">Sterling AI Academy</span>
                  </div>
                </div>
                
                <div className="pt-4 border-t border-gray-100 dark:border-white/5 flex items-center justify-between text.xs font-bold relative z-10">
                  <div className="flex items-center gap-2 text-gray-500 transition-colors">
                    <Calendar className="w-3.5 h-3.5" />
                    <span>{evt.date}</span>
                  </div>
                  <div className="flex items-center gap-2 text-purple-600 dark:text-purple-400 transition-colors">
                    <Clock className="w-3.5 h-3.5" />
                    <span>{evt.time}</span>
                  </div>
                </div>
              </div>
            )})}
          </div>
        )}
      </div>
    </div>
  );
}
