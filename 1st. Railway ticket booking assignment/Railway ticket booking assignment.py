import random
username = ["kunwar", "akash", "harsh"]
option = input("Enter option login or register : ")
if (option == "login"):
  login = input("Enter username : ")
  if login in username:
    def func(n):
      return n.upper()
    x = map(func, ("1. delhi - mumbai", "2. kolkata - banglore",
                   "3. dehradun - lucknow", "4. hydrabad - jaipur", 
                   "5. chennai - patna"))
    print(*list(x),sep='\n')
    loc = int(input("Enter the location serial number : "))
    a = random.randint(900, 3500)
    lambda_fun = lambda a : a + 10
    capcha = (lambda_fun(a))
    print("Your seat number is : ",random.randint(1, 73))
    print("Your coach number is : ",random.randint(1, 13))
    print("Your ticket price is : ", a)
    password = int(input("Enter captcha / your ticket price + 10 : "))
    if password == capcha:
      print("Your ticket is confirmed!")
    else:
      print("Your password / your ticket price is invalid")
  else:
    print("You don't have a username. PLEASE REGISTER")
elif (option == "register"):
  n_user = input("Please create your username : ")
  if n_user in username:
    print("This username is already taken please try again!")
  else:
    username.append(n_user)
    def greet(name):
      print("Your username", n_user, "created successfully!")
    greet(n_user)
else:
  print("Invalid input")
