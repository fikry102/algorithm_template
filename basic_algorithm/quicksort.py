import random

def partition(nums, left, right):
    if left >= right:
        return

    pivot_idx = random.randint(left, right)
    pivot = nums[pivot_idx]
    
    nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            
    partition_idx = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[partition_idx], nums[i] = nums[i], nums[partition_idx]
            partition_idx += 1
            
    nums[right], nums[partition_idx] = nums[partition_idx], nums[right]

    partition(nums, partition_idx + 1, right)
    partition(nums, left, partition_idx - 1)

    return

def quicksort(A):
    partition(A, 0, len(A) - 1)
    return A

if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(quicksort(a))