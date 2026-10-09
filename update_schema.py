import os

path = r'c:\anti\sterlingVM\prisma\schema.prisma'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_models = '''
// Master CRM Lead representing the full funnel
model Lead {
  id              String   @id @default(cuid())
  name            String
  phone           String   @unique
  source          String   @default("Manual") // e.g. "Instagram Ad", "WhatsApp Chat", "Manual"
  campaignId      String?  
  status          String   @default("New") // "New", "Pending AI Call", "Called", "Converted", "Dead"
  aiCallOutcome   String?  // AI's final summary
  lastContactedAt DateTime?
  createdAt       DateTime @default(now())
  updatedAt       DateTime @updatedAt
  
  callTasks       CallTask[]
}

// AI Outbound Call Queue Manager
model CallTask {
  id            String   @id @default(cuid())
  leadId        String
  lead          Lead     @relation(fields: [leadId], references: [id])
  status        String   @default("Pending") // "Pending", "InProgress", "Completed", "Failed"
  scheduledFor  DateTime @default(now())
  attempts      Int      @default(0)
  twilioCallSid String?  
  recordingUrl  String?
  transcript    String?
  createdAt     DateTime @default(now())
  updatedAt     DateTime @updatedAt
}

// Cached Meta Analytics (Aggregated daily)
model MetaAnalytics {
  id            String   @id @default(cuid())
  date          DateTime @unique
  spend         Float    @default(0.0)
  impressions   Int      @default(0)
  clicks        Int      @default(0)
  leadsGen      Int      @default(0)
  waMessages    Int      @default(0)
  igEngagement  Int      @default(0)
  updatedAt     DateTime @updatedAt
}
'''

content = content + new_models

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
