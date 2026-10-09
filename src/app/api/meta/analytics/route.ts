import { NextResponse } from 'next/server';
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
