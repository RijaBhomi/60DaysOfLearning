# A sapm comment id defined as a text containing the following keywords:
# "make a lot of money", "buy now", "subscribe this ", "click here". Write a porgram to detect these spams

p1= "make a lot of money"
p2= "buy now"
p3= "subscribe this "
p4= "click here"

message= input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
    