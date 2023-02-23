# 1 Countdown - 

def countDown(num):
    newList=[]
    for i in range(num,-1,-1):
        newList.append(i)
    return newList
print(countDown(5)) 


# 2 Print and Return - 

def print_and_return(list):
    print(list[0])
    return(list[1])
print(print_and_return([1,2]))


# 3 First Plus Length - 

def firstPlusLength(list):
    return (list[0] + len(list))
print(firstPlusLength([1,2,3,4,5]))


# 4 Values Greater than Second - 

def values_greater_than_second(list):
    newList = []
    if len(list)<2:
        return False
    for i in list:
        if i>list[1]:
            newList.append(i)
    print(len(newList))
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))


# 5 This Length, That Value - 

def length_and_value(len,val):
    newList = []
    for i in range(len):
        newList.append(val)
    return(newList)
print(length_and_value(4,5))
