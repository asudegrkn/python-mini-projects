import string
import random


length = int(input("Şifrenizin uzunluğunu giriniz:"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation

all = lower + upper + num + symbol

randomChar = random.sample(all,length)

password = "".join(randomChar)

print("şifreniz:" + password)