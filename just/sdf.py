def decoder(word):
    wordLength = len(word)
    decodeWord = None;
    if(wordLength > 2):
        if(word[wordLength-2:] == "ay") :
            decodeWord = word[wordLength-3]
            if(wordLength > 3) :
                decodeWord += word[0:wordLength - 3]

    return decodeWord
def incoder(word):
    first = word[0]
    newWord = word[1:] + first + "ay"

    return newWord


word = input("Enter Word")
incodeing = incoder(word)
print(incodeing)
print(decoder(incodeing))