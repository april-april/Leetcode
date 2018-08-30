def reverseString(s):
        arr = list(s)
        i, j  = 0, len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return "".join(arr)

print(reverseString("kiki do you love me")) # em evol uoy od ikik