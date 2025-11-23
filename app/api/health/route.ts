import { checkDatabaseConnection } from '@/lib/db'
import { NextResponse } from 'next/server'

export const runtime = 'nodejs'

export async function GET() {
  const dbStatus = await checkDatabaseConnection()

  return NextResponse.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    database: dbStatus,
    environment: process.env.NODE_ENV,
    version: process.env.npm_package_version || '1.0.0',
  })
}