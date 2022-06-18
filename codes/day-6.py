print ("1 for Addition")
print ("2 for subtraction")
print ("3 for multiplication")
print ("4 for devision")

task = input("please type the number what task you want to perform: ")

if task == "1":
    num1 = int (input("Enter the firs number: "))
    num2 = int (input("Enter the second number: "))
    print ("The sum of the total number is: ",  num1 + num2)


elif task == "2":
    num1 = int (input("Enter the firs number: "))
    num2 = int (input("Enter the second number: "))
    print ("The subtraction of the total number is: ",  num1 - num2)

elif task == "3":
    num1 = int (input("Enter the firs number: "))
    num2 = int (input("Enter the second number: "))
    print ("The multiplication of the total number is: ",  num1 * num2)

elif task == "4":
    num1 = int (input("Enter the firs number: "))
    num2 = int (input("Enter the second number: "))
    print ("The devision of the total number is: ",  num1 / num2)