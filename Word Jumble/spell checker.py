#Programming Exercise 10 - Chap 13
###SPELL CHECKER###

# Spellchecker takes file input and checks each word against dictionary input.
# Non-dictionary words are printed to the screen.

class SpellCheck:
    def __init__(self, infile, dictionary):
        self.dict = dictionary
        self.infile = infile
        self.words = []
        self.text = []
        self.read_inputFile()
        self.read_Dict()
        for word in self.text:
            self.binary_search(self.words, word)

    def read_Dict(self):
        processDict = open(self.dict, 'r').readlines()
        for word in processDict:
            self.words.append(word.strip())     

    def read_inputFile(self):
        processFile = open(self.infile,'r', encoding = "ISO-8859-1").readlines()
        for line in processFile:
            words = line.split()
            for word in words:
                self.text.append(word.strip("!@#$%^&*()'~`><:;,.][}{\|").lower())


    def binary_search(self, wordList, inputWord):
        #Base case: empty word list -> input word's not in dictionary
        if len(wordList) == 0:
            print(inputWord + " is not in dictionary.")
            return False
        else:
            #Find middle of list
            mid = len(wordList) // 2
            word_in_Dict = wordList[mid]
            #if word inputted is in dictionary, return True
            if inputWord == word_in_Dict:
                return True
            else:
                left = wordList[:mid]
                right = wordList[mid+1:]

                if inputWord < word_in_Dict:
                    return self.binary_search(left, inputWord)
                else:
                    return self.binary_search(right, inputWord)         

def main():
    SpellCheck('word cloud.txt', '2of12.txt')
main()
