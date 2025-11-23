import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({
    log: ['query'],
  })

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma

// 处理 Vercel Edge Runtime 的连接管理
if (process.env.NODE_ENV === 'production') {
  // 在生产环境中确保连接被正确关闭
  process.on('beforeExit', async () => {
    await prisma.$disconnect()
  })
}