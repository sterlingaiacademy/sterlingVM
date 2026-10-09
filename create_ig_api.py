import os

os.makedirs(r'c:\anti\sterlingVM\src\app\api\meta\analytics\ig-posts', exist_ok=True)
path = r'c:\anti\sterlingVM\src\app\api\meta\analytics\ig-posts\route.ts'

code = '''import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function GET() {
  try {
    const config = await prisma.systemConfig.findUnique({ where: { key: 'META_CONFIG' } });
    if (!config || !config.value) return NextResponse.json({ error: "Meta account not connected." }, { status: 400 });
    const { access_token } = JSON.parse(config.value);

    // Try to get IG ID directly from config first
    let igAccountId = null;
    const igConfig = await prisma.systemConfig.findUnique({ where: { key: 'META_IG_ACCOUNT_ID' } });
    if (igConfig && igConfig.value) {
        igAccountId = igConfig.value.trim();
    } else {
        // If no IG ID, try to find it via Facebook Page ID
        const fbConfig = await prisma.systemConfig.findUnique({ where: { key: 'META_FB_PAGE_ID' } });
        if (fbConfig && fbConfig.value) {
            const fbRes = await fetch(https://graph.facebook.com/v19.0/?fields=instagram_business_account&access_token=);
            const fbData = await fbRes.json();
            if (fbData.instagram_business_account?.id) {
                igAccountId = fbData.instagram_business_account.id;
            }
        }
    }

    if (!igAccountId) {
        return NextResponse.json({ error: "Instagram Account ID not found. Please add your FB Page ID or IG Account ID to config." }, { status: 400 });
    }

    // Fetch the recent posts, reels, and stories
    const mediaRes = await fetch(https://graph.facebook.com/v19.0//media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,comments_count,like_count&limit=20&access_token=);
    const mediaData = await mediaRes.json();

    if (mediaData.error) {
        return NextResponse.json({ error: mediaData.error.message }, { status: 400 });
    }

    return NextResponse.json({ success: true, data: mediaData.data });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
'''
with open(path, 'w', encoding='utf-8') as f:
    f.write(code)
