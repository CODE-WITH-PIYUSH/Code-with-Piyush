# Software for calculating speed.
print("This software is used to calculate speed.")
c = "Hello user, Enter your name to use this software."
print(c)
a = input("Enter your Name")
b = "Good Morning,"
e = "Please give required data to use this software."
print(b+a)
print(e)
distance = input("Enter the distance you travelled in kms.")
time = input("Enter the hours which you travelled in hrs.")
distance = float(distance)
time = float(time)
result = distance/time
result = str(result)
unit = "KMPH"
print("Your speed is", result + unit)