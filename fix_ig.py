import os

path = r'c:\anti\sterlingVM\src\app\api\meta\campaign\ig-push\route.ts'
content = '''import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import fs from 'fs';
import path from 'path';

export async function POST(req: NextRequest) {
  try {
    const { caption, imageUrl } = await req.json();

    const config = await prisma.systemConfig.findUnique({
      where: { key: 'META_CONFIG' }
    });

    if (!config || !config.value) {
      return NextResponse.json({ error: "Meta account not connected. Please save your System User Token." }, { status: 400 });
    }

    const { access_token } = JSON.parse(config.value);
    const igConfig = await prisma.systemConfig.findUnique({ where: { key: 'IG_ACCOUNT_ID' } });
    const igAccountId = igConfig?.value?.trim();

    if (!igAccountId) {
      return NextResponse.json({ error: "Instagram Account ID is not configured in Account Config." }, { status: 500 });
    }

    let publicUrl = "";

    // If image is a base64 string, we must save it locally and expose it via a public URL because Meta requires a URL for IG
    if (imageUrl && typeof imageUrl === 'string' && imageUrl.startsWith('data:image/')) {
      const matches = imageUrl.match(/^data:([A-Za-z-+\/]+);base64,(.+)$/);
      if (matches && matches.length === 3) {
        const buffer = Buffer.from(matches[2], 'base64');
        const uploadDir = path.join(process.cwd(), 'public', 'uploads');
        if (!fs.existsSync(uploadDir)) {
          fs.mkdirSync(uploadDir, { recursive: true });
        }
        
        const fileName = ig_temp_.jpg;
        fs.writeFileSync(path.join(uploadDir, fileName), buffer);
        
        // Construct the public URL using the request origin
        const origin = req.headers.get('origin') || http://;
        publicUrl = ${origin}/uploads/;
      }
    }

    if (!publicUrl) {
      return NextResponse.json({ error: "Instagram posts require a valid image. Please provide an image." }, { status: 400 });
    }

    // 1. Create Media Container
    const containerRes = await fetch(https://graph.facebook.com/v19.0//media?image_url=&caption=&access_token=, {
      method: 'POST'
    });
    const containerData = await containerRes.json();

    if (containerData.error) {
      return NextResponse.json({ error: Meta API Error:  }, { status: 400 });
    }

    const creationId = containerData.id;

    // 2. Publish the Container
    const publishRes = await fetch(https://graph.facebook.com/v19.0//media_publish?creation_id=&access_token=, {
      method: 'POST'
    });
    const publishData = await publishRes.json();

    if (publishData.error) {
      return NextResponse.json({ error: Publish Error:  }, { status: 400 });
    }

    return NextResponse.json({ 
      success: true, 
      message: "Successfully published post to Instagram!" 
    });

  } catch (error: any) {
    console.error("Instagram Push Error:", error);
    return NextResponse.json({ error: error.message || "Internal Server Error" }, { status: 500 });
  }
}
'''
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
