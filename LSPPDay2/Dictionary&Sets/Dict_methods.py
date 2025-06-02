food={
    "pizza" : 900,
    "Alloo" : 30.0,
    "Shreeja": 100,
    0: "Hi"
}

# print(food.items()) # displays key value pairs in a list of tuples
# print(food.keys()) # displays keys in a list
# print(food.values()) # displays values in a list

#Update the value
food.update({"Shreeja":200, "Rija": "Slayyy"})
print(food)

# Get method - display value of specified keys
#print(food.get("Shreeja2"))  #Prints Non
#print(food["Shreeja2"])  # Returns error

# Remove items
food.pop(0)
print(food)
