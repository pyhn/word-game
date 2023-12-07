class WordsDict:
    def __init__(self, size, filename):
        """Function that initializes a word_game dict object
        input: size of word, filename
        output: none
        """
        file = open(filename, "r") 
        contents = (file.read()).split("\n")
        
        self.size = size
        
        
        word_dict = {}
        
        for line in contents:
            if len(line) > self.size:
                word = line[0:self.size]
                definition = line[self.size:len(line)]   
                
            elif len(line) == self.size:
                word = line.upper()
                definition = line
            
            word_dict[word] = definition     
            
        self.word_dict = word_dict

    def check(self, word):
        """Function that checks if word is in dict
        input: word
        output: true or false 
        """        
        words = list(self.word_dict.keys())
        if word in words:
            return True
        else:
            return False
    
    def getSize(self):
        """Function that returns size of dictionary
        input: none
        output: # of words in dict
        """        
        return len(self.word_dict)
    
    
    def getWords(self, letter):
        """Function that gets a list of words starting with inputed letter
        input: letter
        output: list of matching words
        """        
        words = list(self.word_dict.keys())
        words.sort()
        letter = letter.upper()
        matching_words = []
        for word in words:
            if word[0] == letter:
                matching_words.append(word)            
        return matching_words
            
    
    def getWordSize(self):
        """Function that returns size of words
        input: none
        output: size of words
        """        
        return(self.size)
    
    def getDict(self):
        """Function that returns dictionary of words
        input: none
        output: dictionary
        """          
        return self.word_dict

    
        
if __name__ == "__main__":
    
    # initializes word_game class with word size 5, and openning file "word_game5.txt"
    
    word_game = WordsDict(5, "word_game5.txt")
    
    # test to print if word in dict
    print(word_game.check("hello".upper()))
          
    # test to print size of dictionary
    print(word_game.getSize())
   
    # test to print words starting with letter (z)
    print(word_game.getWords("h"))
    
    # test to print size of word
    print(word_game.getWordSize())
    
    # test to print dict
    #print(scrabble.get_dict())