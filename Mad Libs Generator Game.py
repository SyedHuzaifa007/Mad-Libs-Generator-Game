# Importing Modules

from tkinter import *

# Creating the main Window

root = Tk()
root.geometry('600x600')
root.title('Mad Labs Generator Game')
Label(root,text='Welcome to Mad Libs Generator Game \n Generate Amusing and Funny Stories. Have Fun!',font='arial 10 bold').pack()
Label(root,text='\nClick Anyone of the below button ',font='arial 8 bold').place(x=40, y=40)

# Defining First Function

def madlib1():
    animal = input("Enter an animal name: ")
    place = input("Enter a place name: ")
    profession = input("Enter a profession name: ")
    cloth = input("Enter a cloth name: ")
    thing = input("Enter a thing name: ")
    name = input("Enter a name: ")
    verb = input("Enter a verb in 'ing' form: ")
    food = input("Enter a food name: ")
    print("===============")
    print("READ THIS STORY")
    print("===============")
    print(f"{name} was {verb} when a man came who was {profession} by profession. He was wearing the clothes made up of {cloth}. He had a {thing} in his hand and he told that he has came from {place}. {name.title()} was eating {food} at that time suddenly a {animal} passes from there who eat them both and ran away.")

# Defining Second Function

def madlib2():
    animal = input("Enter an animal name: ")
    place = input("Enter a place name: ")
    profession = input("Enter a profession name: ")
    cloth = input("Enter a cloth name: ")
    things = input("Enter a thing name: ")
    name = input("Enter a name: ")
    verb = input("Enter a verb in 'ing' form: ")
    food = input("Enter a food name: ")
    print("===============")
    print("READ THIS STORY")
    print("===============")
    print(f"Once {name} was sleeping in the {palce}. Dreaming to become a {profession}. Suddenly a {thing} hit on the head of {name}. {name} got up and saw here and ther. {name} saw a {animal} running.{name} picked up {name} and cleaned with {cloth} cloth. {name} hold the {thing} and hit the {animal} with his full strength. The {animal} got injured. {name} picked up the {animal} in the hands and gave {animal} {food} to eat. {animal} ate that {food} upto the fill and ran away {verb}.")

# Defining Third Function

def madlib3():
    animal = input("Enter an animal name: ")
    place = input("Enter a place name: ")
    profession = input("Enter a profession name: ")
    cloth = input("Enter a cloth name: ")
    things = input("Enter a thing name: ")
    name = input("Enter a name: ")
    verb = input("Enter a verb in 'ing' form: ")
    food = input("Enter a food name: ")
    print("===============")
    print("READ THIS STORY")
    print("===============")
    print(f"{name} was going to {place}. {name} dream was to become a {profession} but {name}'s {cloth} was the reason of {name}'s rejection in the every interview. Sometimes {name} was found eating {food} in the office and whenever {name}'s boss called {name}, {name} start {verb}. The boss once gifted {name} a {thing} but {name} refused to accept it by saying 'I want a {animal} in gift.")

# Creating Buttons

Button(root, text = 'Story-1', font = 'arial 15', command = madlib1, bg = 'grey' ).place(x = 60, y = 120)
Button(root, text = 'Story-2', font = 'arial 15', command = madlib2, bg = 'grey' ).place(x = 60, y = 180)
Button(root, text = 'Story-3', font = 'arial 15', command = madlib3, bg = 'grey' ).place(x = 60, y = 240)

# Printing Name

Label(root,text='This Game is made by Syed Huzaifa',font='arial 8 bold').place(x=200, y=500)

# Running Window

root.mainloop()