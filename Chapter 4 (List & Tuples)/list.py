friends = ["Rolf", "Bob", "Jen", "Anne"  "Orange", 5, 3.14, True]

#list mutable hoti hai (matlab change ho sakti hai).

print(friends[0])  # Rolf
print(friends[1])  # Bob    

print(friends[-1])  # True
print(friends[-2])  # 3.14

print(friends[2:5])  # ['Jen', 'Anne', 'Orange']
print(friends[:4])  # ['Rolf', 'Bob', 'Jen', 'Anne']


print(friends[2:])  # ['Jen', 'Anne', 'Orange', 5, 3.14, True]
print(friends[:])  # ['Rolf', 'Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True]
friends[0] = "Smith"

print(friends)  # ['Smith', 'Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True]
friends.append("Smith")
print(friends)  # ['Smith', 'Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True, 'Smith']
friends.insert(1, "Smith")  

print(friends)  # ['Smith', 'Smith', 'Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True, 'Smith']
friends.remove("Smith")

print(friends)  # ['Smith', 'Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True, 'Smith']
friends.pop()  # 'Smith'
print(friends)  # ['Smith', 'Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True]
friends.pop(0)  # 'Smith'



print(friends)  # ['Bob', 'Jen', 'Anne', 'Orange', 5, 3.14, True]
friends.clear()     
print(friends)  # []









