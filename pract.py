
#3.1 Write a program that reads from the console the radius "r" of a circle and prints its
#perimeter and area.
#3.2 Write a program to calculate (a+b)2

import math


# pi = math.pi
# x = int(input('Enter a radius to find the perimeter and area of a circle: '))
#
# diameter = x * 2
#
# perimeter = pi * diameter
#
# rsquare = x * x
#
# area = pi * rsquare
#
# print(f"The perimeter is: {perimeter}")
# print(f"The area is: {area}")

#

# def text():
#     person =  input("Enter person name: ")
#     book = input ("Enter book name: ")
#     sender = "Authors Team"
#     return print(f"Dear {person}.\n We are pleased to inform you that {book} is the best Bulgarian book.\n The authors of the book wish you good luck. \n Yours \n {sender}")
#
# text()





# def calculate(a, b):
#     result = ( a + b) ** 2
#     return result


# a = float(input("Enter a: "))
# b = float(input("Enter b: "))

# results = calculate(a,b)

# print(f"Result for (a + b)**2 is {results}")



# for y in range(4):
#     for x in range(3 - y):
#         print(" ", end="")
#     for k in range(1, 2*y):
#         print("*", end="")
#     print()


# def calculate(x):
#     y = 4*x + 10
#     return print(f"y = {y}")
#
# calculate(5)
#




# def main():
#  print("This program calculates the area of a rectangle or a triangle")
#  print("Enter a and b (for rectangle) or a and h (for triangle): ")
#  a = int(input())
#  b = int(input())
#  print("Enter 1 for a rectangle or 2 for a triangle: ")
#  choice = int(input())
#  area = (a * b) / choice
#  print("The area of your figure is", area)
# if __name__ == "__main__":
#  main()




# *********************






# Practical Excercise 4

#Task 1

# def main():
#   number = int(input("Enter a number: "))
#
#   if number > 0:
#     print(number, "is a positive number")
# if __name__ == "__main__":
#   main()

# # Task 2

# def main():
#    number = int(input("Enter a number: "))
#    if number > 0:
#      print(number, "is a positive number")
#    else:
#      print(number, "is a negative number")
# if __name__ == "__main__":
#  main()


# # Task 3

# def main():
#   number = int(input("Enter a number: "))
#   if number == 10:
#     print("Number is 10")
#   elif number == 20:
#     print("Number is 20")
#   elif number == 30:
#     print("Number is 30")
#   else:
#     print("None of the values is matching to 10, 20 or 30")
#     print("Exact value of a is:", number)
# if __name__ == "__main__":
#  main()


# Exercise

#4.1
# def main():
#   number = int(input("Enter a number: "))
#   if number % 2 == 0:
#     print(number, "is an even number")
#   else:
#     print(number, "is an odd number")
# if __name__ == '__main__':
#   main()


#4.2

# def main():
#   name = input("Enter Name: ")
#   student_id = int(input("Enter Student ID: "))
#   score = int(input("Enter a score: "))

#   def score_cal(self):
#     if score > 85:
#         result = str("HD")
#         #print("Grade: HD")
#     elif score > 75:
#         result = str("D")
#         #print("Grade: D")
#     elif score > 65:
#         result = str("CR")
#         #print("Grade: CR")
#     elif score > 50:
#         result = str("Pass")
#         #print("Grade: Pass")
#     elif score < 50:
#         result = str("Fail")
#         #print("Grade: Fail")

#     return result
  
#   final_score = score_cal(score)
  
#   print(f"Name: {name}\nStudent ID: {student_id}\nResult: {final_score}")

# if __name__ == '__main__':
#   main()



#4.3

# def main():
#   number1 = int(input("Enter a number: "))
#   number2 = int(input("Enter a number: "))
#   number3 = int(input("Enter a number: "))
#   numlst = []
#   numlst.append(number1)
#   numlst.append(number2)
#   numlst.append(number3)
#   maximum = max(numlst)
#   minimum = min(numlst)
#   print(f"Maximum number: {maximum}\nMinimum number: {minimum}")
  
# if __name__ == '__main__':
#   main()




# Practical Exercise 5

#Task 1

# n = int(input("n = "))
# factorial = 1
# while n > 0:
#  factorial *= n
#  n -= 1
# print("n! =", factorial)


# Task 2

# n = long(input("n = "))
# factorial = 1
# while n > 0:
#  factorial *= n
#  n -= 1
# print("n! =", factorial)

# There is no difference between these 2 program as in python3
# long() has been unifies with int() so using long()
# is not neccessary we can usr int() instead


# Task 3
# n = int(input("n = "))
# m = int(input("m = "))
# num = n
# product = 1
# while num <= m:
#  product *= num
#  num += 1
# print("product[n...m] =", product)


# Exercise
#5.1

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))
# num = 1
# product = 1
# while num <= m:
#  product *= n
#  num += 1
# print("n to the power of m: ", product)
 


# Practical Exercise 6

#Task 1

# def main():
#  students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95),
# ("Eva", 88)]
#  for index, (name, score) in enumerate(students):
#   grade = calculate_grade(score)
#   print("Student {}: {}, Score: {}, Grade: {}".format(index, name,
# score, grade))
# def calculate_grade(score):
#  if score >= 90:
#   return "A"
#  elif 80 <= score < 90:
#   return "B"
#  elif 70 <= score < 80:
#   return "C"
#  elif 60 <= score < 70:
#   return "D"
#  else:
#   return "F"
# if __name__ == "__main__":
#  main()


#Task 2
# def main():
#  for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end='')
#     print()
# if __name__ == "__main__":
#     main()

#Task 3

# def main():
#  print("\n\n")
#  print("Display the pattern like pyramid with asterisk:")
#  print("-------------------------------------------------\n\n")
#  rows = int(input("Input number of rows: "))

#  spc = rows + 4 - 1
#  for i in range(1, rows + 1):
#     print(" " * spc, end="")

#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()
#     spc -= 1
# if __name__ == "__main__":
#  main()


# #Task 4 
# def main():
#  print("\n\n")
#  print("Display the number in reverse order:")
#  print("--------------------------------------\n\n")
#  num = int(input("Input a number: "))
#  sum = 0
#  t = num
#  while (t != 0):
#     r = t % 10
#     #print("r= ", r)
#     sum = sum * 10 + r
#     #print("sum= ", sum)
#     t = t // 10
#     #print("t= ",t)
#  print("The number in reverse order is:", sum)
# if __name__ == "__main__":
#  main()


# Exercise 6.1
# ABCD, A+B = C+D

# def main():

#     final_lst = []

#     for i in range(1, 10):
#         for j in range(0,10):
#             for k in range(0,10):
#                 for l in range(0, 10):
#                     if i + j == k + l:
#                         num = i,j,k,l
#                         numbers = int(''.join(map(str, num)))
#                         final_lst.append(numbers)
                    
#     print(final_lst)
# if __name__ == "__main__":
#  main()


#Practical Exercise 7
#Task 1

# def main():
#  array = [1, 2, 3, 4, 5]
#  length = len(array)
#  reversed_array = [0] * length
#  for index in range(length):
#     reversed_array[length - index - 1] = array[index]
#  for index in range(length):
#     print(reversed_array[index], end=" ")

# if __name__ == "__main__":
#  main()


#Task 2

# n = int(input("Enter the number:"))
# array = []
# for i in range(n):
#  array.append(int(input()))


#Task 3

# array = ["one", "two", "three", "four"]
# print(array)
# array1 = ["one", "two", "three", "four"]
# for index in range(len(array1)):
#  print("Element[{}] = {}".format(index, array1[index]))


#Task 4
# print("Enter a positive integer: ")
# n = int(input())
# array = []
# print("Enter the values of the array:")
# for _ in range(n):
#  array.append(int(input()))
# symmetric = True
# for i in range(n // 2):
#     if array[i] != array[n - i - 1]:
#         symmetric = False
#         break
# print("Is symmetric?", symmetric)


#Task 5
# print("Enter the number of the rows: ")
# rows = int(input())
# print("Enter the number of the columns: ")
# cols = int(input())
# matrix = []
# print("Enter the cells of the matrix:")
# for row in range(rows):
#     matrix.append([])
#     for col in range(cols):
#         print(f"matrix[{row},{col}] = ", end="")
#         matrix[row].append(int(input()))
# for row in range(rows):
#     for col in range(cols):
#         print(" ", matrix[row][col], end="")
#     print()


#Task 6
# def main():
#  HEIGHT = 12
#  # Allocate the array in a triangle form
#  triangle = [[0] * (row + 1) for row in range(HEIGHT)]
#  # Calculate Pascal's triangle
#  triangle[0][0] = 1
#  for row in range(HEIGHT - 1):
#     for col in range(row + 1):
#         triangle[row + 1][col] += triangle[row][col]
#         triangle[row + 1][col + 1] += triangle[row][col]
#  # Print Pascal's triangle
#  for row in range(HEIGHT):
#     print(" " * ((HEIGHT - row) * 2), end="")
#     for col in range(row + 1):
#         print(f"{triangle[row][col]:^3}", end=" ")
#     print()
# if __name__ == "__main__":
#  main()


#Exercise
#7.1

#import array as arr

# print("Enter the length of array: ", end="")
# array_len = int(input())
# lst = arr.array('i', [])
# for i in range (1,array_len + 1):
#   print(f"Enter array element {i}: ",end='')
#   lst.append(int(input()))
# print(lst)
# print(type(lst))

#7.2

# matrix = [
#   [1, 2, 3, 4, 5, 6],
#   [6, 5, 4, 3, 2, 1],
#   [9, 8, 7, 6, 5, 4],
#   [4, 5, 6, 7, 8, 9]
# ]
#
# max_sum = -1
# max_submatrix = []
#
# for i in range(len(matrix)-1):
#   for j in range(len(matrix[i]) - 1):
#     sub_matrix = [
#       [matrix[i][j], matrix[i][j+1]],
#       [matrix[i+1][j], matrix[i+1][j+1]]
#     ]
#
#     current_sum = (matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1])
#
#     if current_sum > max_sum:
#         max_sum = current_sum
#         max_submatrix = sub_matrix
#
# print("Ther 2x2 sub-matrix with max sum is: ", end="")
# for row in max_submatrix:
#    print(row)
# print("Maximum sum: ", max_sum)



# Session 8
#Task 1

# class Book:
#   def __init__(self, title, author, year_published):
#     self.title = title
#     self.author = author
#     self.year_published = year_published

#   def display_info(self):
#     print("Title of the Book :", self.title )
#     print("Author of the Book :", self.author )
#     print("Year Published :", self.year_published )


# book = Book('Alchemist','Paulo coelho','1988')
# book.display_info()


#Task 2

# class MovieTicket:
#   def __init__(self, movie_name, customer_name, seat_number):
#     self.movie_name = movie_name
#     self.customer_name = customer_name
#     self.seat_number = seat_number

#   def display_ticket(self):
#     print("Movie Name: ", self.movie_name)
#     print("Customer Name: ", self.customer_name)
#     print("Seat Number: ", self.seat_number)


# ticket = MovieTicket('The Matirx', 'John Doe', 'F-14')
# ticket.display_ticket()



# #Task 3

# class CoffeeOrder:
#   def __init__(self, customer_name):
#     self.customer_name = customer_name
  

#   def select_coffe_type(self):
#     print("select a coffee type: \n option (1)Latte \nOption (2)Cappuccino \n Option (3)Espresso")
#     selected_coffee_option = int(input("Select a coffee from the above option: "))
    
#     if selected_coffee_option == 1:
#       selected_coffee_type = "Latte"
#     elif selected_coffee_option == 2:
#       selected_coffee_type = "Cappuccino"
#     elif selected_coffee_option == 3:
#       selected_coffee_type = "Espresso"
    
#     return selected_coffee_type
  
#   def select_coffe_size(self):
#     print("select a coffee type: \n option (1)Small\nOption (2)Medium \n Option (3)Large")
#     selected_coffee_size_option = int(input("Select a coffee from the above option: "))

#     if selected_coffee_size_option == 1:
#       selected_coffee_type = "Small"
#     elif selected_coffee_size_option == 2:
#       selected_coffee_type = "Medium"
#     elif selected_coffee_size_option == 3:
#       selected_coffee_type = "Large"
    
#     return selected_coffee_type


#   def display_order_detail(self,):
#     coffee_type = self.select_coffe_type()
#     coffee_size = self.select_coffe_size()
#     print("Customer Name: ", self.customer_name)
#     print("Coffee Type: ", coffee_type)
#     print("Coffee Size: ", coffee_size)


# mycoffee = CoffeeOrder('Amaan')
# mycoffee.display_order_detail()




# week 9 task 1

# class Animal:
#   def speak(self):
#     pass


# class Dog(Animal):
#   def speak(self):
#     print("Woof woof")


# chiwawa = Dog()
# chiwawa.speak()



# Task 2

# class Person:
#   def display(self):
#     print("Person Method display called")
#
#
# class Employee(Person):
#   def show(self):
#     self.display()
#
#
# john = Employee()
# john.show()


# Task 3

# class Vehicle:
#   def __new__(cls, name):
#     cls.name = name
#     print("Vehicle created")
#     print('Car name: ', cls.name)


# class Car(Vehicle):
#   def __init__(self):
#     super().__new__()
  

# toyota = Car('toyota')
# toyota


# week 10

# Task 1

from abc import ABC, abstractmethod

# pi = math.pi
#
# class Shape(ABC):
#
#   @abstractmethod
#   def area(self):
#     pass

# class Circle(Shape):
#
#   def __init__(self, radius):
#     self.radius = radius
#
#   def area(self):
#     area = pi*self.radius**2
#     print(f"Area of Circle: {area}")
#
#
# class Rectangle(Shape):
#
#   def __init__(self, length, breadth):
#     self.length = length
#     self.breadth = breadth
#
#   def area(self):
#     area = self.length * self.breadth
#     print(f"Area of Rectangel: {area}")
#
#
# # Task 2
#
# circle = Circle(5)
# rectangel = Rectangle(10,10)
# def print_area(shape):
#   shape.area()
#
# print_area(circle)
# print_area(rectangel)
#
#
# # Task 3

class Animal(ABC):

  @abstractmethod
  def make_sound(self):
    pass

  @abstractmethod
  def move(self):
    pass

class Dog(Animal):

  def make_sound(self):
    print("Bow Bow")

  def move(self):
    print("Dog running")


class Bird(Animal):

  def make_sound(self):
    print("Chirp Chirp")

  def move(self):
    print("Bird flying")



def testanimal(Animal):
  Animal.make_sound()
  Animal.move()


labrodor = Dog()
Cockatoo = Bird()

testanimal(labrodor)
testanimal(Cockatoo)