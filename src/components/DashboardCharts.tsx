"use client";

import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, CartesianGrid, Legend } from "recharts";

const COLORS = ['#9333ea', '#c084fc', '#d8b4fe', '#6b21a8', '#3b0764'];

export function LeadSourceChart({ data }: { data: any[] }) {
  const vehicleCounts: Record<string, number> = {};
  data.forEach((log) => {
    let v = log["Course"]?.trim();
    if (v && v !== "-") {
      // Normalize common duplicates slightly
      
      
      vehicleCounts[v] = (vehicleCounts[v] || 0) + 1;
    }
  });

  // Sort and take Top 5, group rest into "Others"
  const sorted = Object.entries(vehicleCounts).sort((a, b) => b[1] - a[1]);
  const top5 = sorted.slice(0, 5);
  const othersCount = sorted.slice(5).reduce((acc, curr) => acc + curr[1], 0);
  
  const chartData = top5.map(([key, val]) => ({ name: key, value: val }));
  if (othersCount > 0) {
    chartData.push({ name: "Others", value: othersCount });
  }

  return (
    <div className="h-64">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={chartData}
            cx="40%"
            cy="50%"
            innerRadius={55}
            outerRadius={75}
            paddingAngle={5}
            dataKey="value"
            stroke="none"
          >
            {chartData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip 
            contentStyle={{ backgroundColor: '#111', borderColor: '#333', color: '#fff', borderRadius: '8px' }}
            itemStyle={{ color: '#fff' }}
          />
          <Legend 
            layout="vertical" 
            verticalAlign="middle" 
            align="right"
            wrapperStyle={{ fontSize: '11px', color: '#888' }}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export function LeadStatusChart({ data }: { data: any[] }) {
  let showroom = 0;
  let service = 0;
  let open = 0;

  data.forEach((log) => {
    const hasService = log["Call Type"] && log["Call Type"].toLowerCase() === "inbound";
    const hasVisit = log["Final Response"] && log["Final Response"].trim() !== "" && log["Final Response"].trim() !== "-";
    
    if (hasService) service++;
    else if (hasVisit) showroom++;
    else open++;
  });

  const chartData = [
    { name: "Outbound", value: showroom },
    { name: "Inbound", value: service },
    { name: "Open / No Booking", value: open }
  ];

  return (
    <div className="h-64">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={chartData}
            cx="40%"
            cy="50%"
            innerRadius={0}
            outerRadius={75}
            dataKey="value"
            stroke="none"
          >
            <Cell fill="#c084fc" />
            <Cell fill="#2196F3" />
            <Cell fill="#9e9e9e" />
          </Pie>
          <Tooltip 
            contentStyle={{ backgroundColor: '#111', borderColor: '#333', color: '#fff', borderRadius: '8px' }}
            itemStyle={{ color: '#fff' }}
          />
          <Legend 
            layout="vertical" 
            verticalAlign="middle" 
            align="right"
            wrapperStyle={{ fontSize: '11px', color: '#888' }}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
