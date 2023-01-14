# Ask the user their names 
name = input("what's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
name = name.title()

# say hello to the user
print("hellow,", name)


# we can also use like this in a simple way 

name = input("what's your name? ").strip().title()

# say hello to the user 

print(f"hello,{name}")