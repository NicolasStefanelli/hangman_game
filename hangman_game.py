import random

def pick_word(filename):
    word_list = []
    in_file = open(filename, "r")
    for word in in_file:
        the_word = str(word)
        word_list.append(the_word)
    num = int(random.randrange(0,(len(word_list)+1)))
    chosen = word_list[num]
    return chosen


def create_enough_spaces(word):
    empty_list = []
    for i in range(len(word)-1):
        empty_list.append("_")
    return empty_list


def word_into_list(word):
    word_as_list = [] # the word in list form
    for ch in word:
        word_as_list.append(ch)
    return word_as_list

    
def guess_letters(word):
    empty_list = create_enough_spaces(word)  
    word_as_list = word_into_list(word)
    counter = 0 # number of incorrect guesses
    bool = True
    my_string = ""
    for i in range(len(empty_list)):
            my_string = my_string + " " + empty_list[i]
    print(my_string)
    while bool == True:
        g_letter = input("Please Guess a Letter:")
        guess_letter = g_letter.upper()

        if guess_letter in word_as_list:
            for i in range(len(word)):
                if word_as_list[i] == guess_letter:
                    empty_list[i] = guess_letter

        else:
            print("Incorrect!")
            counter = counter + 1
        my_string = ""

        for i in range(len(empty_list)):
            my_string = my_string + " " + empty_list[i]
        print(" ")
        print("Number of attempts left: %i" % (6 - counter))
        print(my_string)
        
        print(" ")
        if "_" not in empty_list and counter < 6:
            return 0
        elif counter > 6:
            return 1  


def play_hangman(filename):
    word = pick_word(filename)
    print(word) # take out when ready to play for real
    result = guess_letters(word)
    if result == 0:
        print("You win!")
    else:
        print("Better luck next time!")


#starter code
# play_hangman("test_words.txt")


    










