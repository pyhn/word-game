import random 

from word_game import WordsDict


def get_random_word(word_game):
    """Function that gets a random word from word_game class
    input: word_game object
    output: random word"""
    
    word_dict = word_game.getDict()
    word_list = list(word_dict.keys())
    word = random.choice(word_list)
    return word

def get_input(attempt, word_game):
    """Function that gets input and raises exceptions when an invalid response is given
    input: attempts, word_game object
    output: guess, exceptions
    """
    guess = (input("Attempt {0:1}: Please enter a five letter word: ".format(attempt))).upper()
    if len(guess) < word_game.getWordSize():
        raise Exception(guess + " is too short.")
    elif len(guess) > word_game.getWordSize():
        raise Exception(guess + " is too long.")  
    elif word_game.check(guess) == False:
        raise Exception(guess + " is not a recognized word.")
    else:
        return guess

def game(word, guess, attempt, gameover, green, orange, red):
    """Game function that plays word_game
    inputs: word, guess, attempts, gameover status, green, orange, red lists
    output: gameover status, attempts"""
    # inspired by https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list
    # counts frequency of a letter in a word, and turns it into dict
    # keys are the letter, count is value

    
    guess_freq = {j:guess.count(j) for j in guess}
    word_freq = {k:word.count(k) for k in word}
    
    
    # make a copy of guess and word to use for green, orange, red lists
    guess_c = guess.copy()
    word_c = word.copy()

    # loops through guess and concatenates number if occurs more than once
    guess_num = 0
    for i in range(len(guess_c)):
        if guess_freq[guess_c[i]] > 1:
            guess_num += 1
            guess_c[i] = guess_c[i]+str(guess_num)
    
    
    # loops through guess and concatenates number if occurs more than once
    word_num = 0
    for m in range(len(word_c)):
        if word_freq[word[m]] > 1:
            word_num += 1
            word_c[m] = word_c[m]+str(word_num)   


    # for loop that iterates through word letters
    for i in range(len(word_c)):
        
        # if letter in correct position
        if guess_c[i] == word_c[i] or guess_c[i][0] == word[i]:
            
            green.append(guess_c[i])
                
        # if letter is in word but not right position
        elif guess_c[i] in word_c or guess_c[i][0] in word:
            if len(guess_c[i]) == 2:
                red.append(guess_c[i])
            else:
                orange.append(guess_c[i])
        # letter not in word at all
        else:
           
            red.append(guess_c[i])
                
        
        
    attempt += 1
    
    

    
    # sort lists alphabetically
    
    green.sort()
    orange.sort()
    red.sort()
    
    
    # print results
    print("".join(guess) +" Green={"+", ".join(green) +"} Orange={"+", ".join(orange) +"} Red={"+", ".join(red)+"}")
    
    

    # if attempts go past 6, end game   
    if attempt > 6:
        gameover == False
        print("Sorry you lose. The word is", "".join(word))
    
    return gameover, attempt


def main():
    """Main function that initializes word_game object, and a few necessary game objects
    input: none
    output: none"""
    word_game = WordsDict(5, "word_game5.txt")
    
    word = get_random_word(word_game)
    
    attempt = 1
    gameover = False
    print("Welcome to the Word Game, You have 7 attempts to guess the word.")
    while not gameover and attempt < 7:
        
        try:
            guess = get_input(attempt, word_game)
            
        except Exception as input_exception:
            print(input_exception.args[0])
            
        else:
            word = list(word)
            guess = list(guess)
            green = []
            orange = []
            red = []            
            
            # if guess matches word stop game
            if guess == word:
                print("Found in {0:1} attempts. Well Done. The Word is {1:5}.".format(attempt, "".join(word)))
                gameover = True
            else: 
                gameover,attempt = game(word, guess, attempt, gameover, green, orange, red)
            
main()


