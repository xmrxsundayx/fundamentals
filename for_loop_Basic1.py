#1 Basic
for i in range(0,151):
    print(i)

#2 multipels of five
for i in range (5,1005,5):
    print(i)

#3 counting, the Dojo way
for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4 whoa. That sucker's huge
sum = 0
for i in range (0, 50000):
    if i % 2 == 1:
        sum += i
print(sum)

#5 Countdown by Fours
for i in range (2018, 0, -4):
    print(i)

#6 flexible counter
low_num=1
high_num=50
multi=6
for i in range(low_num,high_num):
    if i %multi == 0:
        print(i)
