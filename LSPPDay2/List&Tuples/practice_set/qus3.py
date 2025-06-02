# check tuple cant be changed
a=("Rija", 3, True)
a[2]= False  # This will raise a TypeError because tuples are immutable