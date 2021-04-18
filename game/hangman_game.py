import random

def read_file():
    
    with open("data.txt", "r", encoding="utf-8") as f:
        letter = [line for line in f]
        letter = random.choices(letter)
        letter_to_string = "".join(letter)
        letter_to_string = letter_to_string[:letter_to_string.find("\n")]
        return letter_to_string

def play_game():
    flag = True
    letter_to_guess = read_file()
    to_list = list(letter_to_guess)
    guess = list("_" * len(to_list))
    
    #print(to_list)
    while guess != to_list:
        print(to_list)
        print(guess)
        letter_player = str(input("Digita una letra: "))
        for i in range(len(to_list)):
            if letter_player == to_list[i]:
                guess[i] = letter_player
                continue
            else:
                print("Te equivocaste")
        
        print(guess)
    


if __name__ == "__main__":
    play_game()