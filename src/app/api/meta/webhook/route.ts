import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

const VERIFY_TOKEN = "sterling_secure_webhook_token_2026";

// Handles Meta Webhook Verification
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const mode = searchParams.get('hub.mode');
  const token = searchParams.get('hub.verify_token');
  const challenge = searchParams.get('hub.challenge');

  if (mode && token) {
    if (mode === 'subscribe' && token === VERIFY_TOKEN) {
      return new NextResponse(challenge, { status: 200 });
    } else {
      return new NextResponse('Forbidden', { status: 403 });
    }
  }
  return new NextResponse('Bad Request', { status: 400 });
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();

    // 1. WhatsApp Inbound Messages
    if (body.object === 'whatsapp_business_account') {
      for (const entry of body.entry) {
        for (const change of entry.changes) {
          if (change.value && change.value.messages) {
            for (const message of change.value.messages) {
              const customerPhone = message.from;
              const contactInfo = change.value.contacts?.find((c: any) => c.wa_id === customerPhone);
              const customerName = contactInfo?.profile?.name || "Unknown WhatsApp User";

              let replyText = "Clicked Ad";
              if (message.type === 'button') {
                 replyText = message.button.text;
              } else if (message.type === 'text') {
                 replyText = message.text.body;
              }

              console.log(`[LEAD CAPTURED - WA] ${customerName} (${customerPhone}) replied: ${replyText}`);

              const formattedPhone = `+${customerPhone}`;
              
              // Legacy table for backwards compat
              await prisma.webhookLead.create({
                data: { name: customerName, phone: formattedPhone, status: replyText }
              });

              // Master CRM Upsert
              const lead = await prisma.lead.upsert({
                where: { phone: formattedPhone },
                update: { status: "WhatsApp Reply", source: "WhatsApp" },
                create: { name: customerName, phone: formattedPhone, status: "New", source: "WhatsApp" }
              });

              // Push to AI Calling Queue!
              // We check if a pending task already exists to avoid double-queueing
              const existingTask = await prisma.callTask.findFirst({
                where: { leadId: lead.id, status: 'Pending' }
              });
              if (!existingTask) {
                await prisma.callTask.create({
                  data: { leadId: lead.id, status: 'Pending' }
                });
                console.log(`[QUEUE] Lead ${lead.name} added to AI dialing queue.`);
              }
            }
          }
        }
      }
    }
    
    // 2. Facebook/Instagram Lead Forms (leadgen)
    if (body.object === 'page' || body.object === 'instagram') {
      for (const entry of body.entry) {
        for (const change of entry.changes) {
          if (change.field === 'leadgen') {
            const leadId = change.value.leadgen_id;
            const formId = change.value.form_id;
            console.log(`[LEAD CAPTURED - FORM] New lead form submitted! Lead ID: ${leadId}`);
            
            // Note: We need a background job or API fetch here to actually hit Graph API 
            // and exchange the lead_id for the user's name and phone number using the System User Token.
            // For now, we stub it. The full fetch logic will go here.
          }
        }
      }
    }

    return new NextResponse('EVENT_RECEIVED', { status: 200 });
  } catch (error) {
    console.error("Webhook Error:", error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}