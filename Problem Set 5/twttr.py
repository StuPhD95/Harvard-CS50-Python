def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    no_vowel = []
    vowels = ["a","e","i","o","u"]
    for char in word:
        if char.lower() in vowels:
            continue
        else:
            no_vowel.append(char)
    return "".join(no_vowel)

if __name__ == "__main__":
    main()
