from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename = 'superhero')

root.title('TTK Bootstrap!')

#Create a function for button

counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text = 'Hello World!')
    else:
        my_label.config(text = 'Bayag')

#Create a label
my_label = tb.Label(text = 'Hello World!', font=('Calibri', 28), bootstyle = 'primary')
my_label.pack(pady = 50)

#Create a button
my_button = tb.Button(text= 'Click me!', bootstyle = 'success', command = changer)
my_button.pack(pady = 50)

#Create label search

#Create entry field for search

#Create label # of pages

#Create entry field for # of pages

#Create label for 'Generate every:'

#Create entry field for integers for generate every

#Create entry field for unit (minutes,hours,days) in generate every


#Create button for generating sheet
generate_sheet_button = tb.Button(text = 'Generate sheet', bootstyle = 'success',command = )
generate_sheet_button.pack(pady = 50)


root.mainloop()