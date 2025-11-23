#include <stdio.h>

int main() {
    int n;
    printf("请输入一个整数：");
    scanf("%d", n);  // ❌ 这里有错误

    printf("你输入的是：%d\n", n);
    return 0;
}
