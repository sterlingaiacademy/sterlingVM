
const { PrismaClient } = require('@prisma/client');
const crypto = require('crypto');

const prisma = new PrismaClient();

function hashPassword(password) {
  return crypto.createHash('sha256').update(password).digest('hex');
}

async function main() {
  const users = await prisma.user.findMany();
  if (users.length > 0) {
    const user = users[0];
    await prisma.user.update({
      where: { id: user.id },
      data: {
        username: 'admin',
        passwordHash: hashPassword('sterling')
      }
    });
    console.log('Updated user 1 to admin:sterling');
  } else {
    await prisma.user.create({
      data: {
        username: 'admin',
        passwordHash: hashPassword('sterling'),
        role: 'admin'
      }
    });
    console.log('Created user admin:sterling');
  }
}

main().catch(console.error);
