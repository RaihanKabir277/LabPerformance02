
def count(text):
    words = text.lower().split()  
    wordCount = {}

    for word in words:
        word = word.strip(" ")  
        wordCount[word] = wordCount.get(word, 0) + 1  

    return wordCount


text = "do you do did you do "


store = count(text)


print(store)
