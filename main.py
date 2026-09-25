def show_result(result):
    print(result)
    if result == 7082011:
        print("Secret message: Happy birthday, Christian!")

# this funtion adds two numbers,
def add(x,y):
    show_result(x + y)
# this funtion subtracts two numbers,
def sub(x,y):
    show_result(x - y)
# this funtion multiplies two numbers,
def mul(x,y):
    show_result(x*y)
# this funtion divides two numbers,
def div(x,y):
    show_result(x/y)

#################### start of program ####################

print("Welcome to the calculator app.")
print("What would you like to do?")


#print(user_choice)

while(True):
    print("Type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, or (q)uit")
    user_choice = input(": ")
    if user_choice == 'a':
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        add(x,y)
    elif user_choice == 's':
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        sub(x,y)
    elif user_choice == 'm':
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        mul(x,y)
    elif user_choice == "d":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        div(x,y)
    elif user_choice == "q":
        print("Closing program...")
        break
    else:
        print("Are you stupid?")