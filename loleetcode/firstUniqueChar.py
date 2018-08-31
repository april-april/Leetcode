import collections

class Solution(object):    
    def firstUniqChar(self, s):
        self.s=s
        c = collections.Counter(self.s)
        for i,v in enumerate(self.s):
            if c[v] == 1:
                return i
            else:
                continue
        
        return -1
        
if __name__ == '__main__':
    solution = Solution()
    test = 'asdfa'
    solution.firstUniqChar(test)