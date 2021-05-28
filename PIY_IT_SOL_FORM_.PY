from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")

    print(f"{name.get(), phone.get(), gender.get(), mail.get(), D_O_B.get(), problem.get()} ")



    with open("Forms.txt", "a") as f:
        f.write(f"{name.get(), phone.get(), gender.get(), mail.get(), D_O_B.get(), problem.get()}\n ")



root.geometry("644x344")
#Heading
Label(root, text="Welcome to PIYUSH IT SOLUTIONS", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
mail = Label(root, text=" mail ")
D_O_B = Label(root, text="DOB")
problem = Label(root, text="problem")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
mail.grid(row=4, column=2)
D_O_B.grid(row=5, column=2)
problem.grid(row=6, column=2)

# Tkinter variable for storing entries
name = StringVar()
phone = StringVar()
gender = StringVar()
mail = StringVar()
D_O_B = StringVar()
problem = StringVar()



#Entries for our form
nameentry = Entry(root, textvariable=name)
phoneentry = Entry(root, textvariable=phone)
genderentry = Entry(root, textvariable=gender)
mailentry = Entry(root, textvariable=mail)
D_O_Bentry = Entry(root, textvariable=D_O_B)
problementry = Entry(root, textvariable=problem)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
mailentry.grid(row=4, column=3)
D_O_Bentry.grid(row=5, column=3)
problementry.grid(row=6, column=3)



#Button & packing it and assigning it a command
Button(text="Submit to PIYUSH IT SOLUTIONS", command=getvals).grid(row=7, column=3)



root.mainloop()
