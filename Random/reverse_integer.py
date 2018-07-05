"""
Reverse the digits of an integer.
Examples:
123 -> 321
-123 -> -321

"""

def reverse_integer(x):

  reversed = 0
  sign = 1 if x > 0 else -1

  while tmp != 0:
    reversed = reversed * 10 + tmp % 10
    tmp = tmp // 10

  return sign * reversed
