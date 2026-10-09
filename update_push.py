import os

path = r'c:\anti\sterlingVM\src\app\api\meta\campaign\push\route.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = '''import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function POST(req: NextRequest) {
  try {
    const { phoneNumbers, adBody, adFooter, buttonText, buttonUrl, imageBlob, useTemplate, templateName, templateLang } = await req.json();

    const config = await prisma.systemConfig.findUnique({ where: { key: 'META_CONFIG' } });
    if (!config || !config.value) return NextResponse.json({ error: "Meta account not connected." }, { status: 400 });

    const { access_token } = JSON.parse(config.value);
    const phoneConfig = await prisma.systemConfig.findUnique({ where: { key: 'META_PHONE_NUMBER_ID' } });
    const phoneNumberId = phoneConfig?.value?.trim();

    if (!phoneNumberId) return NextResponse.json({ error: "WhatsApp Phone Number ID not configured." }, { status: 500 });

    let mediaId: string | null = null;
    
    // Upload image to Meta Media API if provided
    if (imageBlob && typeof imageBlob === 'string' && imageBlob.startsWith('data:image/')) {
      try {
        const matches = imageBlob.match(/^data:([A-Za-z-+\\/]+);base64,(.+)$/);
        if (matches && matches.length === 3) {
          const mimeType = matches[1];
          const buffer = Buffer.from(matches[2], 'base64');
          const blob = new Blob([buffer], { type: mimeType });
          const formData = new FormData();
          formData.append('messaging_product', 'whatsapp');
          formData.append('file', blob, 'media.jpg');
          
          const uploadRes = await fetch(https://graph.facebook.com/v18.0//media, {
            method: 'POST',
            headers: { 'Authorization': Bearer  },
            body: formData
          });
          const uploadData = await uploadRes.json();
          if (uploadData.id) mediaId = uploadData.id;
        }
      } catch (err) {
        console.error("Failed to upload image:", err);
      }
    }

    let successCount = 0;
    const errors: string[] = [];

    for (const phone of phoneNumbers) {
      const cleanPhone = phone.replace(/[^0-9]/g, '');
      let payload: any;

      if (useTemplate && templateName) {
        // TEMPLATE MODE (Single Unified Bubble)
        payload = {
          messaging_product: "whatsapp",
          recipient_type: "individual",
          to: cleanPhone,
          type: "template",
          template: {
            name: templateName.trim(),
            language: { code: templateLang || "en_US" }
          }
        };

        if (mediaId) {
          payload.template.components = [
            {
              type: "header",
              parameters: [
                {
                  type: "image",
                  image: { id: mediaId }
                }
              ]
            }
          ];
        }
      } else {
        // STANDARD MODE (Dynamic Text + Separated Image)
        payload = {
          messaging_product: "whatsapp",
          recipient_type: "individual",
          to: cleanPhone,
          type: "text",
          text: { preview_url: true, body: adBody || "Hello!" }
        };

        if (mediaId) {
          const imagePayload = {
            messaging_product: "whatsapp",
            recipient_type: "individual",
            to: cleanPhone,
            type: "image",
            image: { id: mediaId }
          };
          await fetch(https://graph.facebook.com/v18.0//messages, {
            method: 'POST',
            headers: { 'Authorization': Bearer , 'Content-Type': 'application/json' },
            body: JSON.stringify(imagePayload)
          });
        }

        if (buttonUrl && buttonText) {
          payload = {
            messaging_product: "whatsapp",
            recipient_type: "individual",
            to: cleanPhone,
            type: "interactive",
            interactive: {
              type: "cta_url",
              body: { text: adBody || "Hello!" },
              footer: adFooter ? { text: adFooter } : undefined,
              action: {
                name: "cta_url",
                parameters: { display_text: buttonText, url: buttonUrl }
              }
            }
          };
          if (!payload.interactive.footer) delete payload.interactive.footer;
        }
      }

      const res = await fetch(https://graph.facebook.com/v18.0//messages, {
        method: 'POST',
        headers: { 'Authorization': Bearer , 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        successCount++;
      } else {
        const err = await res.json();
        const errMsg = err?.error?.message || JSON.stringify(err);
        errors.push(${cleanPhone}: );
      }
    }

    if (successCount === 0 && errors.length > 0) {
      return NextResponse.json({ error: WhatsApp API Error:  }, { status: 400 });
    }
    return NextResponse.json({ success: true, message: Sent to  contacts. });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
