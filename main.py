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
    """归并排序的合并操作"""
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


def linear_search(arr, target):
    """
    线性搜索算法实现
    时间复杂度: O(n)
    空间复杂度: O(1)
    返回目标元素的索引，未找到返回-1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    二分搜索算法实现
    时间复杂度: O(log n)
    空间复杂度: O(1)
    注意：数组必须是有序的，返回目标元素的索引，未找到返回-1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def hash_table_search(arr, target):
    """
    哈希表搜索算法实现
    时间复杂度: 平均 O(1), 最坏 O(n)
    空间复杂度: O(n)
    返回目标元素的索引，未找到返回-1
    """
    # 创建哈希表：元素值 -> 索引
    hash_table = {}
    for i, value in enumerate(arr):
        if value not in hash_table:  # 只存储第一次出现的索引
            hash_table[value] = i

    return hash_table.get(target, -1)


def find_all_indices(arr, target):
    """
    查找所有匹配元素的索引
    时间复杂度: O(n)
    返回包含所有匹配索引的列表
    """
    indices = []
    for i, value in enumerate(arr):
        if value == target:
            indices.append(i)
    return indices


if __name__ == "__main__":
    # 测试数组
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 45, 34, 22]

    print("测试数组:", test_array)
    print("-" * 50)

    # 测试不同搜索算法
    target = 34
    print(f"搜索目标: {target}")

    # 线性搜索
    index = linear_search(test_array, target)
    print(f"线性搜索结果: 找到索引 {index}")

    # 哈希表搜索
    index = hash_table_search(test_array, target)
    print(f"哈希表搜索结果: 找到索引 {index}")

    # 查找所有匹配的索引
    all_indices = find_all_indices(test_array, target)
    print(f"所有匹配的索引: {all_indices}")
    print()

    # 测试二分搜索（需要有序数组）
    sorted_array = quick_sort(test_array.copy())
    print("排序后的数组:", sorted_array)

    binary_result = binary_search(sorted_array, target)
    print(f"二分搜索结果: 在有序数组中找到索引 {binary_result}")
    print()

    # 测试未找到的情况
    not_found = 100
    print(f"搜索不存在的元素: {not_found}")
    linear_not_found = linear_search(test_array, not_found)
    hash_not_found = hash_table_search(test_array, not_found)
    binary_not_found = binary_search(sorted_array, not_found)

    print(f"线性搜索: {linear_not_found} (未找到)")
    print(f"哈希表搜索: {hash_not_found} (未找到)")
    print(f"二分搜索: {binary_not_found} (未找到)")

    print("\n" + "=" * 50)
    print("算法复杂度对比:")
    print("线性搜索:     O(n)")
    print("二分搜索:     O(log n) [需要有序数组]")
    print("哈希表搜索:   平均O(1), 最坏O(n)")
