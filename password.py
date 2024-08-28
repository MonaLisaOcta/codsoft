import string
import random
all = string.ascii_letters + string.digits + string.punctuation
length = int(input("Please enter the length of the password: "))
password = ''.join(random.choices(all, k=length))
print("Your password is:", password)