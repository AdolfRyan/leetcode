def merge(nums: list[int], left: int, mid: int, right: int):
  tmp = [0] * (right - left + 1)
  i, j, k = left, mid + 1, 0
  while i <= mid and j <= right:
    if nums[i] < nums[j]:
      tmp[k] = nums[i]
      i += 1
    else:
      tmp[k] = nums[j]
      j += 1
    k += 1
  while i <= mid:
    tmp[k] = nums[i]
    i += 1
    k += 1
  while j <= right:
    tmp[k] = nums[j]
    j += 1
    k += 1
  for k in range(0, len(tmp)):
    nums[left + k] = tmp[k]

def mergeSort(nums: list[int], left: int, right: int):
  if left >= right:
    return
  mid = left + (right - left) // 2
  mergeSort(nums, left, mid)
  mergeSort(nums, mid + 1, right)
  merge(nums, left, mid, right)
  
def test_merge_sort():
    # 测试 1: 空数组
    nums = []
    print("Before sorting:", nums)
    mergeSort(nums, 0, len(nums) - 1)
    print("After sorting: ", nums)
    assert nums == []

    # 测试 2: 单元素数组
    nums = [1]
    print("Before sorting:", nums)
    mergeSort(nums, 0, len(nums) - 1)
    print("After sorting: ", nums)
    assert nums == [1]

    # 测试 3: 已排序数组
    nums = [1, 2, 3, 4, 5]
    print("Before sorting:", nums)
    mergeSort(nums, 0, len(nums) - 1)
    print("After sorting: ", nums)
    assert nums == [1, 2, 3, 4, 5]

    # 测试 4: 倒序数组
    nums = [5, 4, 3, 2, 1]
    print("Before sorting:", nums)
    mergeSort(nums, 0, len(nums) - 1)
    print("After sorting: ", nums)
    assert nums == [1, 2, 3, 4, 5]

    # 测试 5: 随机数组
    nums = [12, 4, 5, 3, 8, 7]
    print("Before sorting:", nums)
    mergeSort(nums, 0, len(nums) - 1)
    print("After sorting: ", nums)
    assert nums == [3, 4, 5, 7, 8, 12]

    print("All test cases passed!")


# 运行测试函数
test_merge_sort()
