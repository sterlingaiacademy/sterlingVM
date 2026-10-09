import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function POST() {
  try {
    const config = await prisma.systemConfig.findUnique({ where: { key: 'META_CONFIG' } });
    if (!config || !config.value) return NextResponse.json({ error: "Meta account not connected." }, { status: 400 });
    const { access_token } = JSON.parse(config.value);

    const adConfig = await prisma.systemConfig.findUnique({ where: { key: 'META_AD_ACCOUNT_ID' } });
    const adAccountId = adConfig?.value?.trim();

    const today = new Date();
    today.setHours(0, 0, 0, 0);

    let spend = 0, impressions = 0, clicks = 0;

    if (adAccountId) {
      try {
        const insightsRes = await fetch(`https://graph.facebook.com/v19.0/act_${adAccountId}/insights?access_token=${access_token}&date_preset=today&fields=spend,impressions,clicks`);
        const insights = await insightsRes.json();
        
        if (insights.data && insights.data.length > 0) {
          const d = insights.data[0];
          spend = parseFloat(d.spend || '0');
          impressions = parseInt(d.impressions || '0');
          clicks = parseInt(d.clicks || '0');
        }
      } catch(e) {
        console.error("Failed to fetch Ad Insights", e);
      }
    }

    // Since we don't have an IG ID yet, we'll keep leads and WA as a fallback count for today based on CRM 
    const waLeads = await prisma.lead.count({
      where: {
        createdAt: { gte: today },
        source: 'WhatsApp'
      }
    });

    const updated = await prisma.metaAnalytics.upsert({
      where: { date: today },
      update: {
        spend,
        impressions,
        clicks,
        leadsGen: waLeads,
        waMessages: waLeads * 3, // Dummy multiplier for demo funnel
        igEngagement: 0
      },
      create: {
        date: today,
        spend,
        impressions,
        clicks,
        leadsGen: waLeads,
        waMessages: waLeads * 3,
        igEngagement: 0
      }
    });

    return NextResponse.json({ success: true, data: updated });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
