import os

path = r'c:\anti\sterlingVM\src\app\api\outbound\queue\process\route.ts'
os.makedirs(os.path.dirname(path), exist_ok=True)

code = '''import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import { randomUUID } from 'crypto';

export async function GET() {
  try {
    // 1. Fetch next 2 pending tasks
    const tasks = await prisma.callTask.findMany({
      where: { status: 'Pending' },
      take: 2,
      include: { lead: true },
      orderBy: { createdAt: 'asc' }
    });

    if (tasks.length === 0) {
      return NextResponse.json({ message: "Queue is empty." });
    }

    const pyConfig = await prisma.systemConfig.findUnique({ where: { key: 'PYTHON_SERVER_URL' } });
    const agentConfig = await prisma.systemConfig.findUnique({ where: { key: 'ELEVENLABS_AGENT_ID' } });
    
    const PYTHON_SERVER_URL = pyConfig?.value || process.env.PYTHON_SERVER_URL || "http://localhost:8080/outbound";
    const AGENT_ID = agentConfig?.value || process.env.ELEVENLABS_AGENT_ID || "";

    const results = [];

    for (const task of tasks) {
      // Mark as in progress to avoid double-dialing
      await prisma.callTask.update({
        where: { id: task.id },
        data: { status: 'InProgress', attempts: { increment: 1 } }
      });

      const callId = randomUUID();
      const payload = {
        phone: task.lead.phone,
        agent_id: AGENT_ID,
        call_id: callId,
        conversation_variables: {
          Name: task.lead.name,
          Source: task.lead.source,
          Direction: "Outbound",
          direction: "Outbound",
          call_type: "OUTBOUND",
          call_id: callId
        }
      };

      try {
        const response = await fetch(PYTHON_SERVER_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });

        if (response.ok) {
          const result = await response.json();
          await prisma.callTask.update({
            where: { id: task.id },
            data: { 
              status: 'Completed', 
              twilioCallSid: result.call_sid || result.id || callId 
            }
          });
          results.push({ task: task.id, status: 'Success' });
        } else {
          throw new Error(await response.text());
        }
      } catch (error: any) {
        console.error("Queue Dispatch Error:", error);
        await prisma.callTask.update({
          where: { id: task.id },
          data: { status: 'Failed' }
        });
        results.push({ task: task.id, status: 'Failed', error: error.message });
      }
    }

    return NextResponse.json({ processed: tasks.length, results });
  } catch (error: any) {
    console.error("Queue Processor Error:", error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
'''
with open(path, 'w', encoding='utf-8') as f:
    f.write(code)
