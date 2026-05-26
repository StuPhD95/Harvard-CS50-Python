from random import randint


def main():
    score = 0
    n = get_level()
    q = generate_integer(n)
    questions = [f"{q[i]} + {q[i+1]} = " for i in range(0,19,2)]
    answers = [q[i] + q[i+1] for i in range(0,19,2)]
    for i in range(len(questions)):
        for _ in range(3):
            try:
                guess = int(input(f"{questions[i]}"))
                if guess == answers[i]:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        print(f"{questions[i]} {answers[i]}")
    print(f"Score: {score}")

def get_level():
    levels = [1,2,3]
    while True:
        try:
            n = int(input("Level: "))
            if n in levels:
                return n
        except ValueError:
            pass

def generate_integer(level):
        if level == 1:
            q = [randint(0,9) for _ in range(20)]
        elif level == 2:
            q = [randint(10,99) for _ in range(20)]
        else:
            q = [randint(100,999) for _ in range(20)]
        return q

"""
If file is executed as a script, __name__ = __main__
If file is executed as a module, __name__ = __professor__
"""

if __name__ == "__main__": 
    main() # This will not run if script is executed as a module.