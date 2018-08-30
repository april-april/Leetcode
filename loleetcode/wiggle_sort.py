class Solution(object):
    def wiggleSort(self, a):
        if not a:
            return
        n = len(a)
        for i in range(1, n, 2):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
            
            if i + 1 < n and a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        
        return a

if __name__== '__main__':
    solution = Solution()
    testArray = [3,5,2,1,6,4]
    print(solution.wiggleSort(testArray))