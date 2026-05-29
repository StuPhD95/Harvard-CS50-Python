def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    X, Y = fraction.split("/")
    X, Y = int(X), int(Y)
    if Y == 0:
        raise ZeroDivisionError
    if X < 0 or X > Y:
        raise ValueError
    return round(X / Y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
