import string
import random 
if __name__ == "__main__":
    #This shows all lower letters 
    s1 = string.ascii_lowercase
    #This shows all Capital letters  
    s2 = string.ascii_uppercase
    #This shows only digits
    s3 = string.digits
    #This shows all other keys 
    s4 = string.punctuation
    #Ask for length of password
    password_length = int(input("Enter password length\n"))

    s=[]

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    #method 1
    random.shuffle(s)
    print("Your password is: ")
    print("".join(s[0:password_length]))

    #method 2
    print("Your password is: ")
    print("".join(random.sample(s,password_length)))