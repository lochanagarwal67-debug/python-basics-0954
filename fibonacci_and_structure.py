# Fibonacci Series and Structure in Python

# Fibonacci Function
def fibonacci(n):
    a, b = 0, 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Structure-like concept using Class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\n\nStudent Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Main Program
n = 10
fibonacci(n)

student1 = Student("Lochan Agarwal", 1, 85)
student1.display()
