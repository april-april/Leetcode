# Binary Search Template 1
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

testArray = [1, 5, 6, 10, 25, 35, 100, 200, 800]
print(binarySearch(testArray, 200)) #prints 7
print(binarySearch(testArray, 5)) #print 1