import random
# ------ GLOBAL VARIABLES  ----------------
n_attemps = 8
record_wins = 0
record_loses = 0
game_status = "intro"




# -------- GAME CORE -----------------
def game_core():
    wins = 0
    loses = 0
    n_attemps = 8
    word_list = ["python", "java", "swift", "javascript"]
    solution = random.choice(word_list)
    solution_list = list(solution)
    lines = "-" * (len(solution))

    def charposition(string, char):
        pos = []  # list to store positions for each 'char' in 'string'
        for n in range(len(string)):
            if string[n] == char:
                pos.append(n)
        return pos

    lower_case = set('qwertyuiopasdfghjklzxcvbnm')
    all_list = set()
    correct_list = []

    print(lines)

    while n_attemps > 0:
        input_ = input("Input a letter:")

        if len(input_) != 1:
            print("Please, input a single letter.")
        elif input_ not in lower_case:
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            if input_ in all_list:
                print("You've already guessed this letter.")
            # -----------------------
            elif input_ in solution and input_ not in all_list:
                correct_list = (charposition(solution, input_))
                for i in correct_list:
                    lines = lines[:i] + input_ + lines[i + 1:]
                if "-" not in lines:
                    wins += 1
                    print(f"You guessed the word {solution}!\nYou survived!")
                    break
            # -----------------------
            elif input_ not in all_list and input_ not in solution:
                n_attemps -= 1
                print(f"That letter doesn't appear in the word.  # {n_attemps} attempt")
            # -----------------------
            all_list.add(input_)  # the input is taken to a list used to know if the word was already chosen

        if n_attemps > 0:  # for the last chance, if n=0 the program doesen't print lines
            print("")
            print(lines)

    if n_attemps == 0:
        loses += 1
        print("You lost!")
    return wins, loses


# ------ INTRO AND RESULTS--------
def intro():
    global record_wins
    global record_loses
    intro_input = ""

    while intro_input not in ("play", "results", "exit"):
        intro_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if intro_input == "play":
            x, y = game_core()
            record_wins += x
            record_loses += y
            intro()

        elif intro_input == "results":
            print(f'You won: {record_wins} times')
            print(f'You lost: {record_loses} times')
            intro()
        elif intro_input == "exit":
            break


# ------ GAME START ------------
print(f'H A N G M A N  # {n_attemps} attempts\n')
if game_status == "intro":
    intro()

