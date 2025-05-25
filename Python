import random
import time

def stopwatch():
    print("\nStopwatch")
    print("Type 'start' to start and 'stop' to stop.")

    while True:
        sek = input(">>> ").lower()
        if sek == "start":
            print("Stopwatch started... Type 'stop' to stop.")
            start_time = time.time()
            while True:
                command = input(">>> ").lower()
                if command == "stop":
                    end_time = time.time()
                    elapsed = end_time - start_time
                    print(f"Stopped! Elapsed time: {round(elapsed, 2)} seconds.")
                    return
                else:
                    print("Type 'stop' to stop the stopwatch.")
        elif sek == "stop":
            print("Stopwatch has not started yet.")
        else:
            print("Unknown command. Type 'start' or 'stop'.")

def timer():
    print("\nTimer")
    while True:
        try:
            a = int(input("Enter number of seconds (no more than 60): "))
            if a > 60:
                print("Please enter a value no greater than 60.")
                continue
            elif a <= 0:
                print("Enter a positive number.")
                continue
            break
        except ValueError:
            print("Enter an integer!")

    while a > 0:
        print(f"Time left: {a} seconds")
        a -= 1
        time.sleep(1)
    print("Time's up!")

def lottery():
    print("\nWelcome to the 'Lottery' game!")
    print("Guess 3 numbers from 1 to 6!")

    numbers = [random.randint(1, 6) for _ in range(3)]
    guesses = []

    for i in range(1, 4):
        while True:
            try:
                guess = int(input(f"Enter number #{i}: "))
                if 1 <= guess <= 6:
                    guesses.append(guess)
                    break
                else:
                    print("Number must be between 1 and 6!")
            except ValueError:
                print("Enter an integer!")

    if guesses == numbers:
        print("You won! Your prize — $1,000,000")
    else:
        print("No luck this time.")
        print(f"Your numbers:      {guesses}")
        print(f"Correct numbers:   {numbers}")

def life():
    print("\nWelcome to the 'Life' game!")
    print("Choose difficulty: easy, medium, hard")
    a = input(">> ").lower()
    if a == "easy":
        lol = 5
        kek = 6
        print("You were born a politician's son — life is sweet.")
    elif a == "medium":
        lol = 3
        kek = 6
        print("An ordinary life somewhere in Kyiv or another city.")
    elif a == "hard":
        lol = 1
        kek = 6
        print("You were born in Africa — our condolences.")
    else:
        print("Invalid difficulty choice.")
        return

    print("Do you go to school? yes/no")
    i = input(">> ").lower()
    if i == "yes":
        chance = random.randint(lol, kek)
        if chance > 2:
            print("You went to school.")
        else:
            print("The boy was on the path to success...")
    elif i == "no":
        print("The future is in your hands.")

    print("University (yes/no), what will you do in life?")
    ooo = input(">> ").lower()
    while True:
        if ooo == "yes":
            chance = random.randint(lol, kek)
            if chance > 2:
                print("You got accepted for free education — well done!")
                break
            else:
                print("Mom was right — you'll be a janitor (didn't get accepted).")
                tt = input("Maybe try another university hmm yes/no: ").lower()
                if tt == "yes":
                    continue
                else:
                    break
        elif ooo == "no":
            print("You decided not to go to university.")
            break

    print("You have little money. Find a part-time job? yes/no")
    pop = input(">> ").lower()

    io = None

    if pop == "yes":
        chance = random.randint(lol, kek)
        if chance > 5:
            print("Well done, you'll have more cash, maybe lol.")
            io = input("Find a girlfriend or wife? yes/no: ").lower()
        elif 2 < chance <= 5:
            print("You found a cool part-time job, but it takes too much time. Quit university? yes/no")
            pip = input(">> ").lower()
            if pip == "yes":
                io = input("You quit university and live alone. Find a girlfriend or wife? yes/no: ").lower()
            else:
                print("You found another part-time job and finished university, but not very happy with your work.")
                io = input("Time to find a girlfriend or wife? yes/no: ").lower()
        else:
            print("You tried many times but didn’t find a job. Tough luck.")
            io = input("You live alone. Find a girlfriend or wife? yes/no: ").lower()
    elif pop == "no":
        print("You died of hunger. Mom never sent money.")
        return

    if io == "yes":
        print("You met her on a walk. Saw her — fell in love. Now you're together and happy.")
        bolo = input("Describe her hair: ")
        bo = input("Her age: ")
        blo = input("Her character: ")
        print("After a long time, you had a child!")
        children = random.randint(1, 3)
        print(f"You have {children} children.")
        print("Having lived with her a long time, you died happy.")
    elif io == "no":
        if random.random() < 0.2:
            print("You got so bored that your close friend became closer... a bit closer than needed.")
            print("You got used to such relationship and had a child!")
            children = random.randint(1, 3)
            print(f"You have {children} children.")
            print("Having lived with him a long time, you died happy. Or not.")
            if random.random() < 0.1:
                print("You were reborn... and you are Igor. Start over!")
            else:
                print("But that was the end.")
        else:
            print("Being alone isn’t bad — you spend less money.")
            print("You died unhappy.")

def calculator():
    print("\nSimple calculator")
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Choose an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Division by zero is not possible!")
                return
        else:
            print("Unknown operation.")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Please enter numbers only.")

# === Game menu ===
while True:
    print("\n Main Menu")
    print("1 - Lottery")
    print("2 - Life")
    print("3 - Calculator")
    print("4 - Timer")
    print("5 - Stopwatch")
    print("0 - Exit game")
    choice = input("What do you want to play? (1 / 2 / 3 / 4 / 5 / 0): ")
    if choice == "1":
        lottery()
    elif choice == "2":
        life()
    elif choice == "3":
        calculator()
    elif choice == "4":
        timer()
    elif choice == "5":
        stopwatch()
    elif choice == "0":
        print("Thanks for playing! See you!")
        break
    else:
        print("Invalid choice. Try again.")
