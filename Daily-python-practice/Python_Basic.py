from numpy import number


print("hello World")

#integer
x = 5
print(x)
print(type(x))

#float
y = 3.14
print(y)
print(type(y))

#string
name = "Aditya"
print(name)
print(type(name))

#boolean
is_student = True
print(is_student)
print(type(is_student))

# List
fruits = ["apple", "banana" ,"cherry",1,2,3.14,True]
print(fruits)
print(type(fruits))

#Tuple
cooridinates = (10.0, 20.0)
print(cooridinates)
print(type(cooridinates))

#Dictionory
person = {"name": "Aditya", "age": 25}
print(person)
print(type(person))

#operators
a = 10
b = 5

#Arithmetic Operators
addition = a+b #addition operation
subtraction = a-b #subtraction operation
multiplication = a*b #multiplication operation
division = a/b #division operation
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

#comparionson operators
is_equal = a == b #(equal to operator)
#what it does--it check the value of a and b are equal or not if they are equal it will return true otherwise it will return false
print("Is a equal to b?", is_equal)

is_greater = a > b #(greater than operator)
#what it does--it check the value of a is greater than b or not if it is greater it will return true otherwise it will return false
print("Is a greater than b?", is_greater)

is_less = a<b #(less than operator)
#what it does--it check the value of a is less than b or not if it is less it will return true otherwise it will return false
print("Is a less than b?", is_less)

greater_equal = a >= b #(greater than or equal to operator)
#what it does--it check the value of a is greater than or equal to b or not if it is greater than or equal to it will return true otherwise it will return false
print("Is a greater than or equal to b?", greater_equal)

less_equal = a <= b #(less than or equal to operator)
#what it does--it check the value of a is less than or equal to b or not if it is less than or equal to it will return true otherwise it will return false
print("Is a less than or equal to b?", less_equal)  

#logical operators

is_adult = True
has_id = False
can_enter = is_adult and has_id #(logical and operator)
#what it does--it check the value of is_adult and has_id both are true
print("Can enter?", can_enter)

can_enter_or = is_adult or has_id #(logical or operator)
#what it does--it check the value of is_adult and has_id if any one of them is true it will return true otherwise it will return false
print("Can enter with or?", can_enter_or)


#conditional statements

#if statement
age = 20
if age >= 18:
    print("You are an adult.")


#if-else statement
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#if-elif-else statement
age = 67
if age < 18:
    print("You are a minor.")   
elif age < 65:
    print("You are an adult.")
else:    print("You are a senior citizen.")


#loops
for i in range(5):#it will print from 0 to 4 because the range function is exclusive of the end value
    print(i)

for i in range(1, 11):#it will print from 1 to 10 because the range function is exclusive of the end value
    print(i)

for i in range(0, 11 ,2): #it will print with the gap of 
    print(i)

for i in range(10, 0, -1): #it will print from 10 to 1 because the range function is exclusive of the end value and it will decrement by 1
    print(i)

for fruit in fruits: #it will print each fruit in the fruits list
    print(fruit)    

for key in person: #it will print each key in the person dictionary
    print(key)
    print(person[key])

for key, value in person.items(): #it will print each key and value in the person dictionary
    print(key, value)

age =16
while age < 18: #it will print "You are a minor." until the age is less than 18
    print("You are a minor.")
    age += 1 #it will increment the age by 1 in each iteration

"""while True: #it will print "This will run forever." indefinitely because the condition is always true
    print("This will run forever.") """



#functions
def greet(name): #it will print "Hello, name!" where name is the argument passed to the function
    print("Hello,", name)

greet("Aditya") #it will call the greet function and pass "Aditya" as the argument

def add(a,b): #it will return the sum of a and b
    return a + b

result = add(5, 3)#it will call the add function and pass 5 and 3 as arguments and store the result in the variable result
print("The sum is:", result)


#classes and objects
class Person: #it is a class named Person
    def __init__(self, name, age): #it is a constructor method that initializes the name and age attributes of the Person class
        self.name = name
        self.age = age

   


#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"    
print(even_or_odd(4)) #it will print "Even" because 4 is an even number
print(even_or_odd(7)) #it will print "Odd" because 7    

#Create a function that takes a list of numbers and returns the largest number in the list.
def find_largest(numbers):
    if not numbers: #it will check if the list is empty or not
        return None
    largest = numbers[0] #it will initialize the largest variable with the first element of the list
    for num in numbers: #it will iterate through each number in the list
        if num > largest: #it will check if the current number is greater than the largest number found so far
            largest = num #if it is greater, it will update the largest variable with the current number
    return largest #it will return the largest number found in the list

numbers = [3, 7, 2, 9, 5]
print("The largest number is:", find_largest(numbers)) #it will print "The largest

# number is: 9" because 9 is the largest number in the list

    