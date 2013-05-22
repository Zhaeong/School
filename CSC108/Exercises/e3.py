def load_words(fil):
    filestr = fil.read()
    wordlist = filestr.split('\n')
    newdict = {}
    for letter in wordlist:
        if letter != '':
            wordin = letter[0]
            if not newdict.has_key(wordin):
                newdict[wordin] = []
    for word in wordlist:
        if word != '':
            newdict[word[0]].append(word)
    return newdict
    
def get_letter_counts(dictionary):
    newdictionary = dictionary.copy()
    for keys in newdictionary:
        newdictionary[keys] = len(newdictionary[keys])
    return newdictionary

def get_letter_percentage(dictionary,string):
    totalwords = 0
    for keys in dictionary:
        totalwords += dictionary[keys]
    if totalwords != 0 and dictionary.has_key(string) and dictionary != {}:
        return (float(dictionary[string]) / totalwords)*100
    else:
        return 0


if __name__ == "__main__":
    testfile = open('testfile.txt')
    l = load_words(testfile)
    k = get_letter_counts(l)
    p = get_letter_percentage(k,'a')
    d = {}