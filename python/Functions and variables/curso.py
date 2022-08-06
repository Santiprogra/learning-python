# Ask user for their name
name = input("What's your name? ")

#Remove whitespace from str and capitalize user's name
name = name.strip().title()
#name = name.capitalize()
#capitalize = only puts the first letter ne uppercase
#title = capitalize the first letters of each word

#Say hello to user
print("Hello, ", end="")
print(name)
print("Hello,"+ name)
print("Hello,", name)
print("Hello, {name}")
print(f"Hello, {name}")

name1 = input("What's your name? ").strip().title()

#Split user´s name into first name and last name
first, last = name1.split(" ")

print(f"Hello, {first}")
