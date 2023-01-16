# Exercise 2: Print the sum of the current number and the previous number

number1 = input()
sum = 0

print("Printing current and previous number sum in a range(" + number1 + ")")

number1 = int(number1)

for i in range(number1):
    current = i
    if i - 1 < 0:
        previous = 0
    elif i - 1 > 0:
        previous = i - 1
    sum = current + previous
    print("Current Number " + str(current) + " Previous Number  " + str(previous) + "  Sum:  " + str(sum))

