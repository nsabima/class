import random
def open_load_words():
    try:
        with open("words.txt","r") as file:
            word_list=file.read().split()
        return word_list
    except FileNotFoundError:
        return (f"Error, the file not exists.")

def display():
    chosed_word=random.choice(open_load_words())
    print(f"\nThe chosed word is: {chosed_word}\n")
    guesses=10
    Warnings=3
    guessed_letter=set()
    score=0

    while gusse:
        user_input=input("\nEnter a letter you think: ").strip().lower()
        if user_input==chosed_word:
            return ("Well guess. You got 1 score")
            score+=1
            if user_input in guessed_letter:
                print("Wrong. This letter has already chosed.")
                if Warnings>0:
                    Warnings-=1
                    print("You lost a warning")
                else:
                    guesses-=1
                    print("Bad guess")
            guessed_letter.add()
            pass
        else:
            if Warnings>0:
if __name__=="__main__":
    display()
        