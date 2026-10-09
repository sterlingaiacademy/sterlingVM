import base64
import os

path = r'c:\anti\sterlingVM\src\app\api\meta\webhook\route.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# We inject the queue logic right after the lead.upsert
# Wait, I need to capture the upserted lead first.

content = content.replace(
'''              // Master CRM Upsert
              await prisma.lead.upsert({
                where: { phone: formattedPhone },
                update: { status: "WhatsApp Reply", source: "WhatsApp" },
                create: { name: customerName, phone: formattedPhone, status: "New", source: "WhatsApp" }
              });''',
'''              // Master CRM Upsert
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
                console.log([QUEUE] Lead  added to AI dialing queue.);
              }'''
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
