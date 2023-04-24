#!/usr/bin/python3
#create two varaible for user input
Value_1 = int(input("Provide your first number: "))
Value_2 = int(input("Provide your second number: "))
#calculate the remainder post divison
def     postDivisionRemainder(Num_1,Num_2):
        remainder = Num_1 % Num_2
        print("the remainder of those numbers is: " + str(remainder))
#Calculate the divisbility
def     divisibility_of_Num1(Num_1):
        if(Num_1 % 3 == 0):
                Num_1A = int(Num_1 / 3)
                print(str(Num_1) + " is divisible by 3 :" + str(Num_1A) + " times")
                print("First number is divisible by 3")
        else:
                print("First value is not divisible by 3")

def     divisibility_of_Num2(Num_2):
        if(Num_2 % 3 == 0):
                Num_2A = int(Num_2 / 3)
                print(str(Num_2) + " is divisible by 3: " + str(Num_2A) + " times")
                print("Second number is divisible by 3")
        else:
                print("second value is not divisible by 3")
#calling the functions
postDivisionRemainder(Value_1, Value_2)
divisibility_of_Num1(Value_1)
divisibility_of_Num2(Value_2)
