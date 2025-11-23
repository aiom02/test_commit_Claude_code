def quick_sort(arr):
    """
    快速排序算法实现
    时间复杂度: 平均 O(n log n), 最坏 O(n²)
    空间复杂度: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr):
    """
    冒泡排序算法实现
    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr


def merge_sort(arr):
    """
    归并排序算法实现
    时间复杂度: O(n log n)
    空间复杂度: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """归并排序的合并函数"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 测试示例
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36]
    
    print("原始数组:", test_array)
    print("\n快速排序结果:", quick_sort(test_array))
    print("冒泡排序结果:", bubble_sort(test_array))
    print("归并排序结果:", merge_sort(test_array))
    
    # 测试边界情况
    print("\n边界测试:")
    print("空数组:", quick_sort([]))
    print("单元素:", quick_sort([1]))
    print("已排序:", quick_sort([1, 2, 3, 4, 5]))
    print("逆序:", quick_sort([5, 4, 3, 2, 1]))