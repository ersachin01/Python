name = "Sachin"

nameshort = name[0:3] # starts from 0 and ends at 3-1

print(nameshort) # output: Sac

print(name[3:]) # output: hin

print(name[:3]) # output: Sac
print(name[:]) # output: Sachin
print(name[-1]) # output: n
print(name[-3:]) # output: hin
print(name[-3:-1]) # output: hi
print(name[::2]) # output: Scin
print(name[::3]) # output: Sh   
print(name[::-1]) # output: nihcaS
print(name[1:5:2]) # output: ah
print(name[::]) # output: Sachin
print(name[::1]) # output: Sachin
print(name[::0]) # This will raise an error because step cannot be zero
print(name[::2]) # output: Scin
print(name[1:5:2]) # output: ah 