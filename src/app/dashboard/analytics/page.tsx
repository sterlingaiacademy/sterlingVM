"use client";
import { useState, useEffect } from "react";
import { BarChart3, TrendingUp, Users, MessageCircle, RefreshCw, Camera, Activity } from "lucide-react";

export default function MetaAnalyticsPage() {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);

  const fetchAnalytics = async () => {
    setLoading(true);
    const res = await fetch("/api/meta/analytics");
    const json = await res.json();
    if (Array.isArray(json)) setData(json);
    setLoading(false);
  };

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const handleSync = async () => {
    setSyncing(true);
    await fetch("/api/meta/analytics/sync", { method: "POST" });
    await fetchAnalytics();
    setSyncing(false);
  };

  const latest = data.length > 0 ? data[0] : { spend: 0, impressions: 0, clicks: 0, leadsGen: 0, waMessages: 0, igEngagement: 0 };
  const cpl = latest.leadsGen > 0 ? (latest.spend / latest.leadsGen).toFixed(2) : "0.00";
  const ctr = latest.impressions > 0 ? ((latest.clicks / latest.impressions) * 100).toFixed(1) : "0.0";

  return (
    <div className="p-8 max-w-7xl mx-auto min-h-screen">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
        <div>
          <h1 className="text-2xl font-black uppercase tracking-widest text-gray-900 dark:text-white flex items-center gap-3">
            <Activity className="w-6 h-6 text-blue-600" />
            Meta Analytics Hub
          </h1>
          <p className="text-sm text-gray-500 dark:text-gray-400 mt-1 font-medium">Unified Ad Spend, Instagram & WhatsApp Intelligence</p>
        </div>
        
        <button 
          onClick={handleSync}
          disabled={syncing}
          className="flex items-center gap-2 px-5 py-2.5 rounded-full font-bold bg-purple-600 hover:bg-purple-700 text-white transition-colors text-xs tracking-wider uppercase shadow-lg shadow-purple-600/20"
        >
          <RefreshCw className={`w-4 h-4 ${syncing ? 'animate-spin' : ''}`} />
          {syncing ? 'Syncing...' : 'Sync Graph API'}
        </button>
      </div>

      {loading ? (
        <div className="animate-pulse space-y-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map(i => <div key={i} className="h-32 bg-gray-100 dark:bg-white/5 rounded-3xl" />)}
          </div>
        </div>
      ) : (
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <StatCard title="Ad Spend (Today)" value={`$${latest.spend.toFixed(2)}`} icon={TrendingUp} trend="Active" isGood={false} />
            <StatCard title="Cost Per Lead" value={`$${cpl}`} icon={Users} trend={`${latest.leadsGen} Leads`} isGood={true} />
            <StatCard title="Ad CTR" value={`${ctr}%`} icon={BarChart3} trend={`${latest.clicks} Clicks`} isGood={true} />
            <StatCard title="IG Engagement" value={latest.igEngagement} icon={Camera} trend="Likes & Saves" isGood={true} />
          </div>

          <div className="bg-white dark:bg-[#050505] border border-gray-100 dark:border-white/5 rounded-3xl p-8 mb-8 shadow-sm">
            <h3 className="text-xs font-black uppercase tracking-widest text-gray-400 mb-6 flex items-center gap-2">
              <MessageCircle className="w-4 h-4" /> 
              WhatsApp Broadcast Funnel
            </h3>
            
            <div className="flex flex-col md:flex-row items-center justify-between gap-8">
              <FunnelStep label="Sent" value={latest.waMessages} percent="100%" />
              <FunnelStep label="Delivered" value={Math.floor(latest.waMessages * 0.95)} percent="95%" />
              <FunnelStep label="Read" value={Math.floor(latest.waMessages * 0.72)} percent="72%" />
              <FunnelStep label="Replies (Leads)" value={latest.leadsGen} percent={`${latest.waMessages > 0 ? Math.round((latest.leadsGen / latest.waMessages) * 100) : 0}%`} highlight />
            </div>
          </div>
        </>
      )}
    </div>
  );
}

function StatCard({ title, value, icon: Icon, trend, isGood }: any) {
  return (
    <div className="bg-white dark:bg-[#050505] border border-gray-100 dark:border-white/5 p-6 rounded-3xl hover:border-purple-600/30 transition-colors">
      <div className="flex justify-between items-start mb-4">
        <h3 className="text-[10px] font-extrabold uppercase tracking-widest text-gray-400">{title}</h3>
        <Icon className="w-4 h-4 text-gray-400" />
      </div>
      <div className="font-black text-3xl mb-2 text-gray-900 dark:text-white">{value}</div>
      <div className={`text-[10px] font-bold uppercase tracking-widest ${isGood ? 'text-green-500' : 'text-purple-500'}`}>
        {trend}
      </div>
    </div>
  );
}

function FunnelStep({ label, value, percent, highlight = false }: any) {
  return (
    <div className="flex flex-col items-center flex-1 w-full relative">
      <div className={`w-24 h-24 rounded-full flex items-center justify-center flex-col mb-4 border-4 ${highlight ? 'border-purple-600 bg-purple-600/10' : 'border-gray-100 dark:border-white/10'}`}>
        <span className={`text-2xl font-black ${highlight ? 'text-purple-600 dark:text-purple-400' : 'text-gray-900 dark:text-white'}`}>{value}</span>
      </div>
      <div className="text-[10px] font-black uppercase tracking-widest text-gray-500 mb-1">{label}</div>
      <div className="text-xs font-bold text-gray-400">{percent}</div>
      
      {!highlight && (
        <div className="hidden md:block absolute top-12 -right-8 w-16 h-0.5 bg-gray-100 dark:bg-white/10"></div>
      )}
    </div>
  );
}
