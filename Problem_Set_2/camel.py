name = input("camelCase: ")

lst = []
for i in range(len(name)):
    if name[i].isupper() is True:
        lst.append("_"+name[i].lower())
    else:
        lst.append(name[i])
        
lst = "".join(lst)
print("snake_case:", lst)