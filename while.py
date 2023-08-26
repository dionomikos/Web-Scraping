# While - break statement
# One example of its usage is pagination

number = 4

while number > 0:
    print(number)
    number = number - 1
    if number == 2:
        break
print("Loop Ended!")