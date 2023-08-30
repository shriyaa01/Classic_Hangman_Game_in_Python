#Import Required Libraries
import random
#Function for randomly selecting word from list of word
def choose_word():
    programming_languages = ["python", "java", "javascript",  "ruby", "swift", "kotlin", "php",
                             "golang", "rust", "perl", "haskell", "scala", "matlab", "julia", "lua", "typescript",
                             "dart", "groovy", "fortran", "cobol", "lisp", "prolog", "ada", "assembly",
                             "scheme", "clojure"]
    return random.choice(programming_languages)
#Function For Display Word
def display(word,guessed_letters):
    d=""
    for letter in word:
        if letter in guessed_letters:
            d+=letter
        else:
            d+="*"
    return d
#operating function
def hangman():
    word_to_guess=choose_word()
    attempt=5
    guessed_letters=[]
    print("WELCOME TO HANGMAN:)")
    print("Here, we have to guess the programming language.")
    while attempt>0:
        print("\n" + display(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess)>1 or not guess.isalpha():
            print("Enter a single alphabet")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempt -= 1
            print(f"Wrong guess! {attempt} attempts left.")

        if "*" not in display(word_to_guess, guessed_letters):
            print(f"\nCongratulations! You guessed the programming language: {word_to_guess}")
            break

    if attempt==0:
        print(f"\nSorry, you've run out of attempts. The word was: {word_to_guess}")
#Main Body
if __name__=="__main__":
    hangman()