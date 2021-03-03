a = int(input())
b = int(input())
num1 = int(input())

c = int(input())
d = int(input())
num2 = int(input())

X = 0
Y = 0

for x in range(-10, 11):
    for y in range(-10,11):
        if (a*x + b*y - num1) == (c*x + d*y - num2) and (a*x + b*y - num1) == 0:
            X = x
            Y = y
if X != 0 and Y != 0:
    print(X, Y)
else:
    print('No solution')

