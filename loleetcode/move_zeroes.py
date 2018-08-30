class Solution(object):
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums

def main():
    solution = Solution()
    test_array = [0,5,6,7,0,0,3,4,5]
    answer = solution.moveZeroes(test_array)
    print(answer)
    
main()