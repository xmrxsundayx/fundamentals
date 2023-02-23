num1 = 42 #integer
num2 = 2.3 #float
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #list initialize
print(type(fruit)) #log statement, and type check
print(pizza_toppings[1]) #log statement, accessing a list value
pizza_toppings.append('Mushrooms') #adding a list value
print(person['name']) #logging a dictionary value
person['name'] = 'George' #changing dictionary value
person['eye_color'] = 'blue' #adding a dictionary value
print(fruit[2]) #logging a list value

if num1 > 45: #if conditional
    print("It's greater") #log statement
else: #else conditional
    print("It's lower") #log statement

if len(string) < 5: #if conditional
    print("It's a short word!") #log statement
elif len(string) > 15: #else if conditional
    print("It's a long word!") #log statement
else: #else conditional
    print("Just right!") #log statement

for x in range(5): #for loop (5) is a stop
    print(x) #log value
for x in range(2,5): #for loop (2) is a start (5) is a stop
    print(x) #log value
for x in range(2,10,3): #for loop (2) is a start (10) is a stop (3) is an increment
    print(x) #log value
x = 0 #variable declaration
while(x < 5): #while loop (x) start value (5) stop value
    print(x) # lot statement
    x += 1 #increment

pizza_toppings.pop() #deleting last value from pizza_toppings list
pizza_toppings.pop(1) #deleting indicie (1) value from pizza_toppings list

print(person) #log statement 
person.pop('eye_color')  #deleting dictionary value
print(person) #log new statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': #if conditional
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement
        break #break

def print_hello_ten_times(): #function with no parameters
    for num in range(10): #for loop (10) is a stop
        print('Hello') #log statement

print_hello_ten_times() #function argument

def print_hello_x_times(x): #function with parameters (x)
    for num in range(x): #for loop where (x) is a stop
        print('Hello') # log statement

print_hello_x_times(4) # invoke function with an argument

def print_hello_x_or_ten_times(x = 10): #function with paramerters (x=10)
    for num in range(x): #for loop where (x) is a stop
        print('Hello') #log statement

print_hello_x_or_ten_times() #invoke function
print_hello_x_or_ten_times(4) #invoke function with an argument

# this is a single line comment
"""
this is
a multiline
comment
"""
"""  
Bonus section
"""

num3 = 72 # variable declaration
print(num3) # log statement
fruit[0] = 'cranberry' # list change value
print(person['favorite_team']) #log statement of dictionary value
print(pizza_toppings[7])#log statement of list value
print(boolean) #log statemnet of boolean data type
fruit.append('raspberry') #list add value
fruit.pop(1) #list delete value of inicie 1