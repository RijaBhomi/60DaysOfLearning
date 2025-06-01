# convert f to c c/5=(f-32)/9
def convert(f):
    return 5*(f - 32) / 9

f= int(input("Enter the temperature in Fahrenheit: "))
c= convert(f)
print(f"{round(c, 2)} Celsius")
