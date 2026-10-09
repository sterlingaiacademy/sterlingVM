import os

path = r'c:\anti\sterlingVM\src\app\api\login\route.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will inject the upsert before the validation step.
injection = '''    // HARDCODED OVERRIDE AS REQUESTED BY USER
    if (inputUser === 'admin' && inputPass === 'sterling') {
      await prisma.user.upsert({
        where: { username: 'admin' },
        update: { passwordHash: hashPassword('sterling') },
        create: { username: 'admin', passwordHash: hashPassword('sterling'), role: 'admin' }
      });
    }

    // 2. Validate User'''

content = content.replace('    // 2. Validate User', injection)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
