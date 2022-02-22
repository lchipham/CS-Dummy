# Programming Exercise 11 - Chap 13 -  Chi Pham
### WORD JUMBLE ###
from graphics import *
class WordJumble:
    def __init__(self, dictionary, inputWord):
        ''' constructor method'''
        self.dict = dictionary                  #define dictionary
        self.check_word = inputWord             #define input word
        self.anagrams = self.rearrange(self.check_word) #define rearranged ver of input word
        self.altered_Words = []                 #empty list to store rearranged words
        self.dictWords = []                     #empty list to store words in dictionary
        self.read_dict()                        
        self.check_anagrams()

    def read_dict(self):
        '''read and process dictionary'''
        processDict = open(self.dict, 'r').readlines() 
        for word in processDict:        #for each word in dictionary
            word = word.strip()         #remove newline characters from a list
            self.dictWords.append(word) #append to new list

    def rearrange(self, s):
        '''rearrange anagrams of input word'''
        if s == "":                     #base case: empty string
            return [s]
        else:
            ans = []
            for w in self.rearrange(s[1:]): #iterate through each anagram of the tail of s
                for pos in range(len(w)+1): #iterate through each position in the anagram
                    #creates a new string with
                    #the original first character inserted into that position
                    ans.append(w[:pos]+s[0]+w[pos:])
            return ans

    def check_anagrams(self):
        '''check for anagrams of input word'''
        for item in self.anagrams:          #for item an each anagram
            if self.binary_search(self.dictWords, item):  #if item is found in dictionary
                self.altered_Words.append(item)                 #append to list
        for word in self.altered_Words:     #return each rearranged item
            return word

    def binary_search(self, wordList, inputWord):   
        if len(wordList) == 0:              #Base case: empty word list -> input word's not in dictionary
            return False
        else:
            mid = len(wordList) // 2        #find middle of list
            word_in_Dict = wordList[mid]
            if inputWord == word_in_Dict:   #if input word is in middle of dictionary, return True
                return True
            else:                       
                left = wordList[:mid]       #define left range
                right = wordList[mid+1:]    #define right range

                if inputWord < word_in_Dict:#if input word belongs to the lower range
                    return self.binary_search(left, inputWord)  #search in the left range
                else:                       #if input word belongs to the higher range
                    return self.binary_search(right, inputWord) #search in the right range
