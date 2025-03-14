import random
words = ['enum', 'python','colab','vs code', 'game']

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Wellcome to hangman game")
print(" _ " *len(word))

while attempts > 0:
    guess = input("\n guess the letter: ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("write a alphabet only!")
        continue
    if guess in guessed_letters:
        print("this letter is already choose another letter")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -=1
        print(f"wrong {attempts} attempts.")

    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    if"_" not in displayed_word:
        print(f"Congratulations! the word is {word}")
        break        
else:
    print(f"Game over! the correct word is {word}")