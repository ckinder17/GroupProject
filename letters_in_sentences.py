""" PLAIN ENGLISH
start

User will be prompted to enter a sentence.
Using a letter dictionary we will add a value of one to each different letter in the sentence.
One will be added to every reoccuring letter.
We then display the frequency of letters in that sentence in order of the most frequent.
We will not show values of zero and remove them from the sorted list.

end
"""

""" PSUDOCODE
Enter a sentence:
For all letters A - Z, += 1
Display Sorted List
Sort Letter List key = f, reverse = true
If letter frequency != 0, show them on list
"""

def main():
    sentence = input("Enter a sentence: ")
    sentence = sentence.upper()
    letterDict = dict([(chr(n),0) for n in range(65, 91)])
    for char in sentence:
        if 'A' <= char <= 'Z':
            letterDict[char] += 1
    displaySortedResults(letterDict)

def displaySortedResults(dictionaryName):
    letterList = list(dictionaryName.items())
    letterList.sort(key=f,reverse=True)
    for x in letterList:
        if x[1] != 0:
            print("  " + x[0] + ':', x[1])

def f(k):
    return k[1]

main()