def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        array = s.split()
        reverse = reversed(array)
        join = ' '.join(reverse)

        return join

def main():
    test = 'i like turtles'
    answer = reverseWords(test)
    print(answer)

main()
        