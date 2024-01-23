import string
import random

if __name__ == "__main__":
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.digits
    d = string.punctuation
    plen= int(input("Enter password length\n"))
    s = []
    s.extend(list(a))
    s.extend(list(b))
    s.extend(list(c))
    s.extend(list(d))
    print("Your password is: ")
    print("".join(random.sample(s,plen)))

