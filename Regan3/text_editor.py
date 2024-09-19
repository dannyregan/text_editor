import string 
import sys

# Prepare the file to be edited across all functions
def readTextFile():
    text = open('Regan3/spongebob_movie_trans.txt', 'r')
    text = text.read()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    return text

# Save the file and terminate the program.
def saveTextFile(text):
    with open('Regan3/spongebob_movie_trans.txt', 'w') as savedFile:
        savedFile.write(' '.join(text))
        print('File saved.')
        sys.exit()

def displayMenu():
    menuOptions = ['Top 5 Most Common Words', 'How Many Times Does A Word Appear?', 'Top 5 Least Common Words', 'Replace a Word', 'Add Text', 'Delete Text', 'Highlight Text', 'Save File']
    while True:
        # Display the menu options.
        print('=== Edit Menu ===')
        n = 1
        for option in menuOptions:
            print(f'{str(n)}. {option}')
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
    # Creates a dictionary with each word as a key and the occurance of that word as a value. The default occurance is 0. This number will increase each time the word appears in the text.
    for word in text:
        wordCount[word] = wordCount.get(word, 0) + 1
    # Each key-value pair is turned into a tuple (value, key). The tuple is then appended to a list that can then sort the tuples by occurance.
    for key, value in wordCount.items():
        wordCountSorted.append((value, key))
        wordCountSorted.sort(reverse=True)
        wordCountSorted = wordCountSorted[0:5]
    for item in wordCountSorted:
        print(f"Word: '{str(item[1])}'  Occurances: {str(item[0])}")
    
def SingleWordCount(text):
    while True:
        targetWord = input("What word would you like to search for? ")
        # Check that the user only entered a single word.
        if len(targetWord.split()) == 1:
            targetWord = targetWord.lower()
            if targetWord in text:
                print(f'{targetWord.upper()} appears in the text {str(text.count(targetWord))} times.')
            else:
                print(f'{targetWord.upper()} appears in the text 0 times.')
            return text
        else:
            print('Enter a single word.')

def LeastCommonWords(text):
    wordCount = {}
    wordCountSorted = []
    # Creates a dictionary with each word as a key and the occurance of that word as a value. The default occurance is 0. This number will increase each time the word appears in the text.
    for word in text:
        wordCount[word] = wordCount.get(word, 0) + 1
    # Each key-value pair is turned into a tuple (value, key). The tuple is then appended to a list that can then sort the tuples by occurance.
    for key, value in wordCount.items():
        wordCountSorted.append((value, key))
        wordCountSorted.sort()
    for item in wordCountSorted[0:5]:
        print("Word: '" + str(item[1]) + "'  Occurances: " + str(item[0]))

def ReplaceWord(text):
        targetWord = input("What word would you like to replace? ").lower()
        if targetWord in text:
            replacement = input("What word would you like to replace it with? ").lower()
            # Look through the text one word at a time. Each time you come across the target word, replace it and add 1 to the counter.
            count = 0
            for i in range(len(text)):
                if text[i] == targetWord:
                    text[i] = replacement
                    count += 1
            print(f"The text has been updated. {replacement.upper()} replaced {targetWord.upper()} {count} times.")
        else:
            print(targetWord.upper(), 'does not appear in the text.')
        return text

def AddText(text):
    additions = input('What text would you like to add? ').lower()
    # Split the user's text into words and add them to the end of the text.
    additions = additions.split()
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
            # Look through the text one word at a time. Each time you come across the target word, highlight it.
            for i in range(len(text)):
                if text[i] == targetWord:
                    text[i] = f'**{targetWord.upper()}**'
            print("The text has been updated. " + targetWord.upper() + ' has been highlighted.')
            return text
        else:
            print(targetWord.upper() + ' does not appear in the text. Try again.')

def chooseMenuOption(selection, text):
    # Subtract 1 from their selection to match it to the correct index below.
    selection = selection - 1
    # The functions list contains the name of functions.
    functions = [AllWordCount, SingleWordCount, LeastCommonWords, ReplaceWord, AddText, DeleteText, HighLight]
    # For each selection, add "(text)" to the function name to call the function.
    # Call the function and update the text variable with the new return. These selections are ones that alter the text
    if selection >= 3 and selection != 7:
        text = functions[selection](text)
    elif selection == 7:
        saveTextFile(text)
    # These selections don't alter the text, so saving the return is not required.
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