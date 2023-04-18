# Counter 5.py
def Count(str):
    alpha,upper,lower,number,special = 0,0,0,0,0
    for i in range(len(str)):
        if str[i].isalpha():
            alpha += 1
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower +=1
        elif str[i].isdigit():
            number += 1
        elif str[i]!=" ":
            special += 1
    print('Digits:', number)
    print('Alphabets:', alpha)
    print('Special characters:', special)
    print('Lowercase:', lower)
    print('Uppercase:', upper)
str = input("Enter a string: ")
Count(str)


# Pattern 5.py
import math
N, M = map(int, input("Enter N and M: ").split())
for i in range(0,math.floor(N/2)):
    s= '.|.'*i
    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))
print ('WELCOME'.center(M,'-'))
for i in reversed(range(0,math.floor(N/2))):
    s = '.|.'*i
    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))