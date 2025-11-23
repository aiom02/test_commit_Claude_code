/** @type {import('next').NextConfig} */
const nextConfig = {
  // 确保 Prisma 客户端不被包含在浏览器包中
  webpack: (config, { isServer }) => {
    if (isServer) {
      return config
    }

    // 在客户端构建中排除 Prisma
    config.resolve.fallback = {
      ...config.resolve.fallback,
      fs: false,
      net: false,
      tls: false,
      crypto: false,
      'prisma': false,
      '@prisma/client': false,
    }

    return config
  },

  // 实验性功能
  experimental: {
    serverComponentsExternalPackages: ['@prisma/client'],
  },

  // 环境变量配置
  env: {
    NEXTAUTH_URL: process.env.NEXTAUTH_URL,
  },
}

module.exports = nextConfig