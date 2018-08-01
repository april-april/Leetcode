# Given a time represented in the format "HH:MM", 
# what was the last time that could be displayed 
# using the same subset of digits


class Solution:
    def nextClosestTime(self, time):        
        s = set(time)
        hour = int(time[0:2])
        minute = int(time[3:5])
        while True:
            minute -= 1
            if minute == 60:
                minute = 0
                hour = 0 if hour == 23 else hour + 1
            
            time = "%02d:%02d" % (hour, minute)
            # checks whether every element in set(time) is in s
            # equivalent to set(time).issubset(s)
            if set(time) <= s:
                return time
        
        
def main():        
    solution = Solution()
    time = solution.nextClosestTime('11:36')
    print(time) # prints 11:33
    
main()