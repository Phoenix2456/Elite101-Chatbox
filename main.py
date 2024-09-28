welcome = "Welcome to Elite 101 Chatbot "
print(welcome)
name = input("What's your name? ")
age = int(input(f"Nice to meet you {name}. How old are you? "))
print ("How may I be of help to you today?")

def menu():
  choices = [
    "1. Placeholder Option 1", 
    "2. Placeholder Option 2",
    "3. PLaceholder Option 3", 
    "4. Exit the conversation"
  ]
  
  print("Please choose from the following")
  for options in choices:
    print(options)
  choices = input("Enter your number choice: ")
  
  if choices == "1":
      print("Choice not available")
  elif choices == "2":
      print("Choice not available")
  elif choices == "3":
      print("Choice not available")
  elif choices == "4":
      print(f"Have a great day {name}")
  else:
    print("Please pick a number from the menu")
    

menu()
