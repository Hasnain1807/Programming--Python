import matplotlib.pyplot as plt
import numpy as np


def starpyramid():
    for i in range(1, 10):
        for j in range(1, i):
            print("*", end="")
        print()


def starpyramid2():
    for i in range(1, 10):
        for j in range(i, 9):
            print("*", end="")
        print()


def calc():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Press 1 for addition, /n Press 2 for subtraction, /n Press 3 for multiplication, /n Press 4 for division ")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        print(a + b)
    elif ch == 2:
        print(a - b)
    elif ch == 3:
        print(a * b)
    elif ch == 4:
        print(a / b)
    else:
        print("Invalid choice")


def plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def plot_bar():
    names = ["A", "B", "C", "D", "E", "F"]
    marks = [60, 70, 12, 42, 90, 19]
    plt.bar(names, marks, color=["red", "green", "blue", "yellow", "orange"])
    plt.xlabel("Names")
    plt.ylabel("Marks")
    plt.title("Bar Chart")
    plt.show()


def plot_line():
    days = [1, 2, 3, 4, 5]
    temp = [20, 22, 44, 65, 19]
    plt.plot(days, temp, color="red", linestyle="--", linewidth=3)
    plt.xlabel("Days")
    plt.ylabel("Temperature")
    plt.show()


def num():
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a * 2)
    print(a[1:4])
    print(a.ndim)
    print(a.shape)
    print(a.size)
    print(a.dtype)
    print("----------------------------------------------")
    b = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(b.ndim)
    print(b.shape)
    print(b.size)
    print(b.dtype)
    print("----------------------------------------------")
    c = a.reshape(2, 3)
    print(c)


def oops():
    class student:
        def __init__(self, name, age, math, phy, chem):
            self.name = name
            self.age = age
            self.math = math
            self.phy = phy
            self.chem = chem

        def intro(self):
            print(f"My name is {self.name} and my age is {self.age} ")

        def marks(self):
            print("Total marks are", (self.math + self.phy + self.chem) / 3)

    s1 = student("Hasnain", 19, 75, 78, 93)
    s1.intro()
    s1.marks()


oops()
