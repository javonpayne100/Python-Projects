#Javon Payne
#06OCT2020
#JumbleGame






import random

WORDS = ("cat", "dog", "duck", "feed", "texture", "conservation", "circle", "quota", "chemistry", "provoke", "relevance")
HINTS = ("Meows.",
         "Barks.",
         "Quacks.",
         "A verb.",
         "Can feel it.",
         "To save or keep.",
         "A shape.",
         "Police need it.",
         "Science class.",
         "To start something or encourage.",
         "Of matter or apart of the subject."
         
         )
choice = 'y'
overallScore = 0
while choice.lower() == 'y':
    score = 10
    wordIndex = random.randrange(len(WORDS))

    word = WORDS[wordIndex]
    hint = HINTS[wordIndex]

    
    jumble = ""
    correct = word
    
    #wrong = Sorry, thats not it.
    while word:
        position = random.randrange(len(word)) 
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("""           
           __     __  __     __    __     ______     __         ______    
          /\ \   /\ \/\ \   /\ "-./  \   /\  == \   /\ \       /\  ___\   
         _\_\ \  \ \ \_\ \  \ \ \-./\ \  \ \  __<   \ \ \____  \ \  __\   
        /\_____\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_____\ 
        \/_____/   \/_____/   \/_/  \/_/   \/_____/   \/_____/   \/_____/ 
                                                                  
          """)
    print("\n\t\t\tWelcome to the Word Jumble!")
    print("\t\tUnscramble the letters to make a word")
    print("\t\t\t(Type 'hint' for a hint)")
    print("\nThe jumble is:", jumble)

    guess = input("\nGuess the word: ")

    if guess.lower() == "hint":
        print(hint)
        score -= 4
    elif guess == correct:
        print("correct")
    elif guess != correct:
        print("Sorry, thats not it.")
    
    
    while guess.lower() != correct.lower():
        guess = input("Guess the word: ")
        score -= 1
        if guess == correct:
            print("Correct")
        if guess.lower() == "hint":
            print(hint)
            score -= 4
        elif guess != correct:
            print("Sorry, thats not it.")
    
    print("You guessed it!")
    overallScore += score
    print("Score:", score)
    print("Overall:", overallScore)
    choice = input("\nWould you like to jumble another word? (Y/N) ")
else:
        print("")
    
   
        

