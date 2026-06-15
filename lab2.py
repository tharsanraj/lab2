#get L And B and print square when its same and rectangle if its not same
length = int(input("Enter the length: "))
breath = int(input("Enter the breath: "))
if length == breath:
    print("square")
else:
    print("REctangle")


#2
num = int(input("Enter your number: "))
if num*num < 50:
    print("Less than 50")
else:
    print("Above 50")

#3
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 - num2 == 0:
    print("Its same number")
else:
    print("its not the same number")

#4
mark = int(input("Enter Computer science Mark: "))
if mark >= 50:
    print("Pass")
else:
    print("fail")

#5
num = int(input("Enter a number: "))
if num//10:
    print("yes divisible")
else:
    print("NO not divisible")

#6
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 > num2:
    print("num1 is greater: ", num1)
elif num2 > num1:
    print("num2 is greater: ", num2)
else:
    print("both are equal")

#7
num = int(input("Enter a number: "))
if num ==1:
    print("you can go out and play")
else:
    print("you cannot go out and plaY")


#8
num = int(input("pick a number: "))
if num == 1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")

#9
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
op = input("Enter your operation(+,-,*,/): ")
if op == "+":
    print("Ans =", num1 + num2)
elif op == "-":
    print("Ans =", num1 - num2)
elif op == "*":
    print("Ans =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Ans =", num1/num2)
    else:
        print("Division by 0 is not allowed")
else:
    print("Invalid operation")

#10
booking = input("Enter booking type (O for ordinary, E for Express: )")
weight = float(input("Enter weight of the parcel: "))
if booking == "O":
    if weight <= 5:
        print("charge = 50")
    elif weight <= 10:
        print("charge = 100")
    else:
        print("charge = 150")

elif booking == "E":
    if weight <= 5:
        print("charge = 100")
    elif weight <= 10:
        print("charge = 200")
    else:
        print("charge = 300")

else:
    print("Invalig booking")

#11
price = float(input("Enter the price of the Laptop: "))
if price > 50000:
    discount = price*0.10
else:
    discount = price*0.05
total_price = price - discount
print("price of laptop: ", price)
print("Discount: ", discount)
print("Total price: ", total_price)
                

