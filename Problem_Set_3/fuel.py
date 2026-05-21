while True:
    try:
        fraction = input("Fraction: ")
        num, den = fraction.split("/")
        num, den = int(num), int(den)

        if num < 0 or num > den:
            continue # skip this iteration and start the next iteration of the while loop.

        frac = num/den * 100

        if frac <= 1:
            print('E')
            break
        elif frac >= 99:
            print('F')
            break
        else:
            print(round(frac), end="%")
            break

    except (ValueError, ZeroDivisionError):
        pass