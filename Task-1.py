import random

words = ["python", "apple", "school", "laptop", "camera"]

word = random.choice(words)

guessed = ["_"] * len(word)

wrong_guesses = 0

used_letters = []

print("===== HANGMAN GAME =====")

while wrong_guesses < 6 and "_" in guessed:
    
    print("\nWord:", " ".join(guessed))
    
    letter = input("Enter a letter: ").lower()
    
    
    if letter in used_letters:
        print("You already guessed this letter")
        continue
    
    used_letters.append(letter)
    
    
    if letter in word:
        
        for i in range(len(word)):
            
            if word[i] == letter:
                guessed[i] = letter
        
        print("Correct Guess")
    
    
    else:
        
        wrong_guesses += 1
        
        print("Wrong Guess")
        print("Remaining Chances:", 6 - wrong_guesses)


if "_" not in guessed:
    print("\nCongratulations! You Won")
    print("The word was:", word)

else:
    print("\nGame Over")
    print("The word was:", word)
