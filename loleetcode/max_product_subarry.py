def maxProduct(nums):
    
    maximum=big=small=nums[0]
    
    for n in nums[1:]:
        big, small=max(n, n*big, n*small), min(n, n*big, n*small)
        maximum=max(maximum, big)
        
    return maximum
    

if __name__== '__main__':
    input = [2,3,-2,7,4]
    print(maxProduct(input))