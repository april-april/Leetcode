def is_palindrome_permutation(strng):
    cache = set()
    for char in strng.lower():
        if char in cache:
            cache.remove(char)
        else:
            cache.add(char)

    return len(cache) <= 1
    
is_palindrome_permutation('RACECAR')