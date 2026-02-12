name = "Sachin"

print(len(name)) # output: 6

print(name.endswith("in")) # output: True
print(name.endswith("in", 0, 5)) # output: False
print(name.endswith("in", 0, 6)) # output: True

print(name.startswith("Sa")) # output: True
print(name.startswith("Sa", 0, 5)) # output: True           
print(name.startswith("Sa", 0, 2)) # output: True
print(name.startswith("Sa", 0, 1)) # output: False  