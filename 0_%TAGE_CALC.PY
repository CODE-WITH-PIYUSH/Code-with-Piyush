from tkinter import *

root = Tk()

# Here i am making the percentage calculator
a = input("Enter marks here")
b = input("Enter out of which you got")
a = int(a)
b = int(b)
c = a/b*100
print("Your percentage is",c)
root.geometry("644x344")
#Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)