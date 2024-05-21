# DIGIBHEM
import random
import string
pass_len = 12
password_contents = string.digits + string.ascii_letters + string.ascii_uppercase + string.ascii_uppercase
password = ""
for i in range(pass_len):
    password+=random.choice(password_contents)
print("Your Randomo Password is : ",password)
