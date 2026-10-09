import os

path_get = r'c:\anti\sterlingVM\src\app\api\meta\analytics\route.ts'
code_get = '''import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function GET() {
  try {
    const analytics = await prisma.metaAnalytics.findMany({
      orderBy: { date: 'desc' },
      take: 30
    });
    
    return NextResponse.json(analytics);
  } catch (error) {
    return NextResponse.json({ error: "Failed to fetch analytics" }, { status: 500 });
  }
}
'''
with open(path_get, 'w', encoding='utf-8') as f:
    f.write(code_get)

path_sync = r'c:\anti\sterlingVM\src\app\api\meta\analytics\sync\route.ts'
code_sync = '''import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function POST() {
  try {
    const config = await prisma.systemConfig.findUnique({
      where: { key: 'META_CONFIG' }
    });

    if (!config || !config.value) {
      return NextResponse.json({ error: "Meta account not connected." }, { status: 400 });
    }

    const { access_token } = JSON.parse(config.value);

    // TODO: In production, fetch live Graph API insights for Ads, Instagram, and WhatsApp here.
    // For now, we simulate a successful fetch and generate some realistic dummy data for today.
    // const res = await fetch(https://graph.facebook.com/v19.0/act_<AD_ACCOUNT_ID>/insights?access_token=\);
    
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const updated = await prisma.metaAnalytics.upsert({
      where: { date: today },
      update: {
        spend: 42.50,
        impressions: 12500,
        clicks: 450,
        leadsGen: 12,
        waMessages: 85,
        igEngagement: 320
      },
      create: {
        date: today,
        spend: 42.50,
        impressions: 12500,
        clicks: 450,
        leadsGen: 12,
        waMessages: 85,
        igEngagement: 320
      }
    });

    return NextResponse.json({ success: true, data: updated });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
'''
with open(path_sync, 'w', encoding='utf-8') as f:
    f.write(code_sync)
