// 部署测试脚本
// 运行命令: node scripts/test-deployment.js [your-domain]

const https = require('https');

async function testHealthEndpoint(domain) {
  const url = `https://${domain}/api/health`;

  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const result = JSON.parse(data);
          resolve(result);
        } catch (error) {
          reject(new Error(`Failed to parse JSON: ${error.message}`));
        }
      });
    }).on('error', (error) => {
      reject(new Error(`Health check failed: ${error.message}`));
    });
  });
}

async function testUsersEndpoint(domain) {
  const url = `https://${domain}/api/users`;

  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const result = JSON.parse(data);
          resolve({
            status: res.statusCode,
            data: result,
            headers: res.headers
          });
        } catch (error) {
          reject(new Error(`Failed to parse JSON: ${error.message}`));
        }
      });
    }).on('error', (error) => {
      reject(new Error(`Users API test failed: ${error.message}`));
    });
  });
}

async function main() {
  const domain = process.argv[2];

  if (!domain) {
    console.error('❌ 请提供域名: node test-deployment.js your-domain.vercel.app');
    process.exit(1);
  }

  console.log(`🧪 测试部署在: https://${domain}`);
  console.log('─'.repeat(50));

  try {
    // 测试健康检查端点
    console.log('📊 测试健康检查端点...');
    const healthResult = await testHealthEndpoint(domain);
    console.log('✅ 健康检查通过:', healthResult.database.status);

    // 测试用户 API
    console.log('\n👥 测试用户 API...');
    const usersResult = await testUsersEndpoint(domain);
    console.log('✅ 用户 API 状态:', usersResult.status);
    console.log('📝 返回数据类型:', Array.isArray(usersResult.data) ? '数组' : typeof usersResult.data);

    if (usersResult.status === 200) {
      console.log(`🎉 部署测试成功！数据库连接正常，API 响应正确。`);
    } else {
      console.log(`⚠️  API 响应状态: ${usersResult.status}`);
      console.log('响应数据:', usersResult.data);
    }

  } catch (error) {
    console.error('❌ 测试失败:', error.message);
    console.log('\n🔧 可能的解决方案:');
    console.log('1. 检查环境变量是否正确设置');
    console.log('2. 确认 Vercel 部署是否完成');
    console.log('3. 验证数据库连接字符串');
    console.log('4. 查看函数日志获取详细错误信息');
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { testHealthEndpoint, testUsersEndpoint };