print("Q1:", "variable are containers used to store data types")

print("Q2:", "my_name")

name = "David"
print("Q3:", name)  #output = David

print("Q4:", "Hello is a primitive datatype")
print("Q5:", "25 is an integer")
print("Q6:", "3.14 is a float")
print("Q7:", "True is a boolean")
print("Q8:", "Integers are whole number while float are decimal numbers")

x = 10
y = 5
print("Q9:", x + y) #Output = 15

x = 10
y = 3
print("Q10:", x % y) # Output = 1

print("Q11:", "Arithemetic operators is used for exponentiation")

print("Q12:", "= is used to assign a value to a variable while == is used to compare values if see they are equal")

x = 10
x += 5
print("Q13:", x) # Output = 15

age = 18
print("Q14:", age > 16) #Output = true

a = 10
b = 20
print("Q15:", a == b) # Output = false

print(" Q16:", "A list is an array  assigned to a variable using bracket []")

fruit = ["apple","banana", "orange"]
print("Q17:",fruit)

fruits = ["Apple", "Banana", "Orange"]
print("Q18:", fruits[0]) # apple

numbers = [10, 20, 30, 40]
print("Q19:",  numbers[2])  #30

print("Q20:", "How to add an item to the end of a list is to use append() ")


numbers = [1, 2, 3]
numbers.append(4)
print("Q21:", numbers)  # [1, 2, 3, 4]

print("Q22:", "To remove an item from a list  is to use remove()")

names = ["John", "Mary", "Peter"]
names.remove("Mary")
print("Q23:", names) #['John', 'Peter']

print("Q24:", "The sort() method is used to rearrange a value in a given list")
print("Q25:", "The reverse() method is used to reverse an oreder from a list")
def greet():
    print("Q26:", "Hello")
greet()

print("Q27:" "to package reusuable code under so you can run it anytime")

def add(a, b):
    return a + b

result = add(5, 3)
print("Q28:", result) #8


numbers = [2, 4, 6]

def double(number):
    return number * 2

print("Q30:", double(numbers[1])) #8

students = ["John", "Mary", "David"]
students.append("Sarah")
students.remove("John")
students.sort()

print(students)  # ['David', 'Mary', 'Sarah'] We used append to add "sarah" and used remove to remove "john" and then reaarrange it