welcome = "Welcome to Elite 101 Chatbot "
print(welcome)
name = input("What's your name? ")
age = int(input(f"Nice to meet you {name}. How old are you? "))
print ("How may I be of help to you today?")

menu = [
    "1. Placeholder Option 1", 
    "2. Placeholder Option 2",
    "3. PLaceholder Option 3", 
    "4. Exit the conversation"
]

print("Please choose from the following: ")
for f in menu:
    print(f)
choice = int(input("Enter your number choice: "))

if choice == "1.":
    print("Choice not available")
elif choice == "2.":
    print("Choice not available")
elif choice == "3.":
    print("Choice not available")
elif choice == "4.":
    print(f"Have a great day {name}")
else:
    print("Please choose a number")