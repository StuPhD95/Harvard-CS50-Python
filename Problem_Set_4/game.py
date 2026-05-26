import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

target = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue # Restart the loop.
        elif guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass