import string 
import sys

def readTextFile():
    text = open('Regan3/spongebob_movie_trans.txt', 'r')
    text = text.read()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    return text

def saveTextFile(text):
    with open('Regan3/spongebob_movie_trans.txt', 'w') as savedFile:
        savedFile.write(' '.join(text))
        print('File saved.')
        sys.exit()

def displayMenu():
    menuOptions = ['Top 5 Most Common Words', 'How Many Times Does A Word Appear?', 'Top 5 Least Common Words', 'Replace a Word', 'Add Text', 'Delete Text', 'Highlight Text', 'Save File']
    while True:
        print('=== Edit Menu ===')
        n = 1
        for option in menuOptions:
            print(str(n) + ". " + option)
            n += 1
        try:
            selection = int(input("Select an option from the Edit Menu: "))
            if 1 <= selection <= len(menuOptions):
                return selection
            else:
                print(f'Enter a number between 1 and {len(menuOptions)}')
        except:
            print("Error. Please enter a number from the menu options.")

def AllWordCount(text):
    wordCount = {}
    wordCountSorted = []
    for word in text:
        wordCount[word] = wordCount.get(word, 0) + 1
    for key, value in wordCount.items():
        wordCountSorted.append((value, key))
        wordCountSorted.sort(reverse=True)
        wordCountSorted = wordCountSorted[0:5]
    for item in wordCountSorted:
        print(f"Word: '{str(item[1])}'  Occurances: {str(item[0])}")
    
def SingleWordCount(text):
    while True:
        targetWord = input("What word would you like to search for? ")
        if len(targetWord.split()) == 1:
            targetWord = targetWord.lower()
            if targetWord in text:
                print(f'{targetWord.upper()} appears in the text {str(text.count(targetWord))} times.')
            else:
                print(f'{targetWord.upper()} appears in the text 0 times.')
            return text
        else:
            print('Enter a single word.')

def ReplaceWord(text):
    while True:
        targetWord = input("What word would you like to replace? ").lower()
        if targetWord in text:
            replacement = input("What word would you like to replace it with? ").lower()
            count = 0
            for i in range(len(text)):
                if text[i] == targetWord:
                    text[i] = replacement
                    count += 1
            print(f"The text has been updated. {replacement.upper()} replaced {targetWord.upper()} {count} times.")
            return text
        else:
            print(targetWord.upper(), 'does not appear in the text. Try again.')

def AddText(text):
    additions = input('What text would you like to add? ').lower()
    # Split the new text into words
    additions = additions.split()
    # Add the new words to the existing text list
    text.extend(additions)
    print('Your text has been added.')
    return text
    
def DeleteText(text):
    deletions = input('What text would you like to delete? ').lower()
    if deletions in text:
        text.remove(deletions)
        print(f"The first occurrence of '{deletions.upper()}' has been deleted.")
    else:
        print(f"'{deletions}' does not appear in the text. Try again.")
    return text

def HighLight(text):
    while True:
        targetWord = input("What word would you like to highlight? ").lower()
        if targetWord in text:
            for i in range(len(text)):
                if text[i] == targetWord:
                    text[i] = f'**{targetWord.upper()}**'
            print("The text has been updated. " + targetWord.upper() + ' has been highlighted.')
            return text
        else:
            print(targetWord.upper() + ' does not appear in the text. Try again.')

def LeastCommonWords(text):
    wordCount = {}
    wordCountSorted = []
    for word in text:
        wordCount[word] = wordCount.get(word, 0) + 1
    for key, value in wordCount.items():
        wordCountSorted.append((value, key))
        wordCountSorted.sort()
    for item in wordCountSorted[0:5]:
        print("Word: '" + str(item[1]) + "'  Occurances: " + str(item[0]))

def chooseMenuOption(selection, text):
    selection = selection - 1
    functions = [AllWordCount, SingleWordCount, LeastCommonWords, ReplaceWord, AddText, DeleteText, HighLight]
    if selection >= 3 and selection != 7:
        text = functions[selection](text)
    elif selection == 7:
        saveTextFile(text)
    else:
        functions[selection](text)
    return text
    
def main():
    text = readTextFile()
    while True:
        selection = displayMenu()
        text = chooseMenuOption(selection, text)

# ======================================================================================================================
main()