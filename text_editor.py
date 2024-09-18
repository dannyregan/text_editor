""" 
Create a text editor program, to do this create (or select a text file) to edit. The program will read in this text file in and store the text. It will then present a menu to the user to manipulate the file. Note if using an existing file it must accompany your program such that your program can hardcode the location when run, if a file is created ensure it is creating the file in the same folder as the .py file (in both cases the program should run without editing the file location). The program itself should have the following functions and provide the user to edit the text in the following ways:

A 'AllWordCount' function which will count the frequency of each word in the file and output the top 5 most common words that appear.
Function 'SingleWordCount' will ask the user for a word as input (check to make sure is a single word, you might want to create a function to handle input is a single word) and output the number of times that word appears.
'ReplaceWord' will take a word as input and take another input as a replacement. It will replace the word and output the number of words changed.
The Function 'AddText' will add text to the existing text in the file
The 'DeleteText' function will take as input text and delete the first instance of that text from the file
The function 'HighLight' which will take an input word and then output the text with all instances of that word surrounded by symbols to make it easier to see.
example start text: "Hello this is tom and this is ann, we are both students"
example output text highlighting 'this': "Hello **this** is Tom and **this** is Ann, we are both students"
Lastly there should be a function 'readTextFile' that reads the file and stores it for use in the program and another function 'saveTextFile' that will save all changes made to the text and should be called after all changes to the text.
"""
import string 

def readTextFile():
    text = open('spongebob_movie_trans.txt', 'r')
    text = text.read()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    return text

def displayMenu():
    menuOptions = ['Top 5 Most Common Words', 'How Many Times Does A Word Appear?', 'Replace a Word', 'Add Text', 'Delete Text', 'Highlight Text', 'Top 5 Least Common Words']
    n = 1
    print('=== Edit Menu ===')
    for option in menuOptions:
        print(str(n) + ". " + option)
        n += 1
    selection = eval(input("Select an option from the Edit Menu: "))
    return selection

def AllWordCount(text):
    wordCount = {}
    wordCountSorted = []
    for word in text:
        wordCount[word] = wordCount.get(word, 0) + 1
    for key, value in wordCount.items():
        wordCountSorted.append((value, key))
        wordCountSorted.sort(reverse=True)
        wordCountSorted = wordCountSorted[0:5]
    print(wordCountSorted)
# def SingleWordCount():

# def ReplaceWord():

# def AddText():

# def DeleteText():

# def HighLight():

# def LeastCommonWords():

def chooseMenuOption(selection, text):
    selection = selection - 1
    functions = [AllWordCount(text)]
                 # , SingleWordCount(), ReplaceWord(), AddText(), DeleteText(), HighLight(), LeastCommonWords()]
    return functions[selection]
    
def main():
    while True:
        text = readTextFile()
        selection = displayMenu()
        chooseMenuOption(selection, text)


# ==============================================
main()