#Given a string containing just the characters 
# '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        dict = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
            
        return stack == []


''' 
Add left handed parentheses to the stack as they are encountered. 
If we encounter a right hand parentheses, 
check if the stack is empty (meaning we didn't previously encounter its match) 
or if the stack's top element is its pair. 
At the end return True if the stack is empty
'''

class Solution2(object):
    def isValid2(self, s):
        d = {'{':'}', '(':')', '[':']'}
        stack = []
        for parens in s:
            if parens in d:
                stack.append(parens)
            elif not stack or parens != d[stack.pop()]:
                return False
        return not stack

if __name__ == '__main__':
    solution2 = Solution2()
    testString = '[([()])]'
    print(solution2.isValid2(testString))

