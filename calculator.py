
print("Calculator v1.0")
print( )


num1 = input("Insert a Number: ")
variable = input("Insert a variable(+, -, *, /): ")
num2 = input("Insert a number: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if variable == "+":
    print ("your result: add")

elif variable == "-":
        print(subtract)

elif variable == "*":
    print(multiply)

elif variable == "/":
    print(divide)

else:
  print("error! invalid input")