def reverseWords(s):
    split = s.split()
    reverse = reversed(split)
    new = ' '.join(reverse)
    return new
    
def main():
    lol_string = 'python is awesome'
    print(reverseWords(lol_string))
    
main()