import turtle
#print(another_module.another_variable)
#old where we import module and from that module call a particular class or anything that they want to use from the module

#2nd approach n latest approach
# from turtle import Turtle, Screen
# timmy = Turtle()  #Here timmy object is calling the Turtle class
# timmy.shape("turtle")
# timmy.color('blue')
# print(timmy.forward(100))


# #object and attribute, like objects can be used to call the attributes
# #Like below is the example
# my_screen= Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick() #Will stop the screen unless


#A function tied to an object is known as method!
#Also check once how packages are installed in pycharm like go inside projects and inside you will get couple options where you can see the choices

from prettytable import PrettyTable
table = PrettyTable() #object for prettytable class with name table

#Here we can also add column wise in the table
table.field_names=["Pokemon","Type"]
table.add_rows(
    [
    ["Pikachu", "Euro"],
    ["Squirtle", "wide"],
    ["Charmander", "kimo"],
    ]
)
table.align = "r"
print(table)


