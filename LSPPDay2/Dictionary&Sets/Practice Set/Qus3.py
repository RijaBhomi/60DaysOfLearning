s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # Output: 2, because 20 and 20.0 are considered the same in a set, but "20" is a different type