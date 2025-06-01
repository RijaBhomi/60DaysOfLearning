# Multiplication Table of given no. using For loop
'''
num= int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(f"{num}* {i}= {num*i}")

'''


# using While loop
num= int(input("Enter a number to print its multiplication table: "))
i= 1
while i<=10:
    print(f"{num}* {i}= {num*i}")
    i += 1