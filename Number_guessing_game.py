import random

def guess_the_number():
    play_more = "yes"
    while play_more == "yes":
        num = random.randint(1, 100)
        attempts = 10
        print(f"{'*'*20} Guess The Number Game {'*'*20}")
        while attempts != 0:
            try:
                guess = int(input("Enter a Number Between 1 to 100 :- "))
                if 1 <= guess <= 100:
                    attempts-=1
                    if guess > num:
                        print(f"Too High Guess! {attempts} attempts baki.")
                    elif guess < num:
                        print(f"Too Low Guess! {attempts} attempts baki.")
                    else:
                        print(f"Right Answer! {10-attempts} attempts mein kiya Bhai!")
                        break
                else:
                    print("Enter a Number Between 1 to 100 !")
            except ValueError:
                print("Enter a Number only!")
        if attempts == 0 and num != guess:
            print("You Lose! Better Luck Next Time.")
            print(f"Correct Guess Number is :- {num}")
            
        play_more = input("Do you want to play more? (yes/no) :- ")

def main():
    guess_the_number()
    
if __name__ == '__main__':
    main()