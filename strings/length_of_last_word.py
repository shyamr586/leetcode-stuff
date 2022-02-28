# Problem asks to return length of the last word of a string, considering it has many spaces.

def lastWordlen(word):
    return len(word.split()[-1])

if __name__ == '__main__':
    word1 = "Good Morning   Vietnaaaaaaaaaaaam   "
    word2 = "That was a Wu-tang reference       of another reference."
    word3 = ".split() splits a string. The default parameter are spaces."

    print (f"{word1}:\nLength of last word: {lastWordlen(word1)}\n")
    print (f"{word2}:\nLength of last word: {lastWordlen(word2)}\n")
    print (f"{word3}:\nLength of last word: {lastWordlen(word3)}\n")