string = input("Input: ").strip()
vowels = ("a","e","i","o","u")

lst = []
for i in range(len(string)):
    if string[i].lower() in vowels:
        continue
    else:
        lst.append(string[i])
        
no_vowels = "".join(lst)
print(no_vowels)