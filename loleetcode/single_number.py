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


# second way with hashmap
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

def main():
    test = [4,1,2,1,2]
    print(singleNumber(test))
    version2 = Solution()
    print(version2.singleNumber(test))

main()

# simpler solution
def find_single_number(list):
    hash = {}
    
    for number in list:
        if number in hash:
            hash[number] += 1
        else:
            hash[number] = 1

    for key, value in hash.items():
        if value == 1:
            print(key)
            return key

def main2():
    test = [1, 1, 2, 2, 4, 11, 4, 5, 10, 5, 10]
    answer = find_single_number(test)
    print(answer)

main2()
