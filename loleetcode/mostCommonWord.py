#amazon
#solution from leetcode

""" Split words by space in paragraph and remove all punctuations,
Create new paragraph containing word that are not in banned list,
Calculate number of appereance of each word in new para and save it in a map,
Return the word from map with highest occurence value """

def mostCommonWord(paragraph, banned):

        ban = set(banned)
        paragraph = [s.strip("!?',;.") for s in paragraph.lower().split(' ')]        
        p = [w for w in paragraph if w not in ban]
        word_count = {w: 0 for w in p}
        
        for w in p:
            word_count[w] += 1
        return max(word_count, key=lambda k: word_count[k])

def main():
    sentence = "Bob hit a ball, the hit BALL flew far after it was hit."
    nope = ["hit"]
    answer = mostCommonWord(sentence, nope)
    print(answer)

main()