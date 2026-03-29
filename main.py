class Employee:
    def __init__(self):
        self.name = "John Doe"
    def print_name(self):
        print(self.name)

emp1 = Employee()
print(emp1.name)

# Static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, without creating an instance of the class.
# Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables.
class Test:

    @staticmethod
    def add(a, b):
        print(a + b)
Test.add(1, 2)

# Instance method is a method that belongs to an instance of a class.
# It can access and modify the instance's attributes and can be called on an instance of the class.
# class Test:
#
#     def show(self):
#         print("Instance method")
# #
# t = Test()
# t.show()
#
# # Class method is a method that belongs to the class rather than an instance of the class.
# # It can be called on the class itself, without creating an instance of the class.
# class Test:
#
#     count = 10
#     @classmethod
#     def show(cls):
#         print(cls.count)

name = "madam"
print(name[::-1]) #to reverse the string

# pallindrome
if name == name[::-1]:
    print("it's pallindrome")
else:
    print("its not pallindrome")

# find largest number in list
numbers = [3, 5, 1, 9, 2]
largest = numbers[0]  # Assume the first number is the largest
for number in numbers:
    if number > largest:
        largest = number
print("The largest number is:", largest)

print(max(numbers))

