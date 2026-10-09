import os

path = r'c:\anti\sterlingVM\src\app\api\login\route.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_override = '''    // HARDCODED OVERRIDE AS REQUESTED BY USER
    // 1. Wipe out any old 'mahindra' users or other legacy accounts automatically
    await prisma.user.deleteMany({
      where: { username: { not: 'admin' } }
    });

    if (inputUser === 'admin' && inputPass === 'sterling') {
      // 2. Upsert admin account
      await prisma.user.upsert({
        where: { username: 'admin' },
        update: { passwordHash: hashPassword('sterling') },
        create: { username: 'admin', passwordHash: hashPassword('sterling'), role: 'admin' }
      });
    }'''

content = content.replace('''    // HARDCODED OVERRIDE AS REQUESTED BY USER
    if (inputUser === 'admin' && inputPass === 'sterling') {
      // 1. Wipe out any old 'mahindra' users or other legacy accounts
      await prisma.user.deleteMany({
        where: { username: { not: 'admin' } }
      });
      
      // 2. Upsert admin account
      await prisma.user.upsert({
        where: { username: 'admin' },
        update: { passwordHash: hashPassword('sterling') },
        create: { username: 'admin', passwordHash: hashPassword('sterling'), role: 'admin' }
      });
    }''', new_override)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
