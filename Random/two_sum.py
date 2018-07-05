#brute force

def two_sum(numbers, target):

  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target:
        return True

  return False

#optimized O(n)

def two_sum2(numbers, target):

  s = set()

  for num in numbers:
    if (target - num) in s:
      return True
    s.add(num)
    
  return False