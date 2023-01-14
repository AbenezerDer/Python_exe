# we use input for the user to insert an input

x = input("what's x? ")
y = input("what's y? ")

# we use int for thr py to detect (x) is a number not avariable in this case 
z = int(x) + int(y)
print(z)

# float

x = input("what's x? ")
y = input("what's y? ")

# we use round for the system python to choose weather it is float or integer 
# we use f to insert the , or . after three zeros 
z = round(x + y)
print(f"{z:,}")