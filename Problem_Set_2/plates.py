def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return first_req(s) and second_req(s) and third_req(s) and fourth_req(s)
              
def first_req(s):
    return s[0:1].isalpha()
          
def second_req(s):
    if 2 <= len(s) <= 6:   
        return True
    else:
        return False
    
def third_req(s):
    for i in range(2,len(s)):
        if s[i].isnumeric():
            return s[i] != "0" and s[i:].isnumeric()
    return True
    
def fourth_req(s):
    return s.isalnum()

main()