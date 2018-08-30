"""
Reverse the digits of an integer.
Examples:
123 -> 321
-123 -> -321

"""

def reverse_integer(x):

  reversed = 0
  #sign if it is positive vs negative
  sign = 1 if x > 0 else -1
  tmp = abs(x)

  while tmp != 0:
    reversed = reversed * 10 + tmp % 10
    tmp = tmp // 10

  return sign * reversed

  #test
print(reverse_integer(-123) == -321)
