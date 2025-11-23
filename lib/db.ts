import { prisma } from './prisma'

// 数据库连接健康检查
export async function checkDatabaseConnection() {
  try {
    await prisma.$queryRaw`SELECT 1`
    return { status: 'healthy', timestamp: new Date().toISOString() }
  } catch (error) {
    console.error('Database connection error:', error)
    return {
      status: 'error',
      error: error instanceof Error ? error.message : 'Unknown error',
      timestamp: new Date().toISOString()
    }
  }
}

// 安全的数据库操作包装器
export async function safeDbOperation<T>(
  operation: () => Promise<T>,
  errorMessage: string = 'Database operation failed'
): Promise<{ success: boolean; data?: T; error?: string }> {
  try {
    const data = await operation()
    return { success: true, data }
  } catch (error) {
    console.error(errorMessage, error)
    return {
      success: false,
      error: error instanceof Error ? error.message : errorMessage
    }
  }
}

// Vercel 无服务器函数优化
export const dbConfig = {
  // 连接池配置（适用于 PlanetScale, Supabase 等）
  connectionLimit: 10,

  // 查询超时配置
  queryTimeout: 10000, // 10秒

  // 针对不同环境的优化
  development: {
    logQueries: true,
    errorFormat: 'pretty' as const,
  },

  production: {
    logQueries: false,
    errorFormat: 'minimal' as const,
  },
}

// 获取当前环境配置
export function getDbConfig() {
  const isProduction = process.env.NODE_ENV === 'production'
  return isProduction ? dbConfig.production : dbConfig.development
}