class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        max_sub = current

        for i in nums[1:]:
            current = current + i
            if i > current:
                current = i
            if current > max_sub:
                max_sub = current
        return max_sub

def main():
    solution = Solution()
    test_array = [-2,1,-3,4,-1,2,1,-5,4,-4,4000]
    print(solution.maxSubArray(test_array))

main()
