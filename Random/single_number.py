# Given a non-empty array of integers, every element appears
# twice except for one. Find that single one.

# bit manipulation solution using XOR
def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = 0

        for number in nums:
            bit ^= number

        return bit

def main():
    test = [4,1,2,1,2]
    print(singleNumber(test))

main()

# second way

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
