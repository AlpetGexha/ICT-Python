with open('words.txt', 'r') as fd:
    word_list = fd.read().split()


def is_trip_pair(wordList):
    for word in wordList:
        i = 0
        pairCount = 0
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                pairCount += 1
                if pairCount == 3:
                    print(word)
                i += 2
            else:
                pairCount = 0
                i += 1


is_trip_pair(word_list)
