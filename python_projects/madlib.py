# Importing all modules
from tkinter import *

# Creating a GUI master window and placing all its components
root = Tk()

# Setting the title of the main window
root.title("Python Mad Libs Generator")
# Setting the dimensions of the main window
root.geometry('360x300')
# Setting the background color of the main window
root.config(background="#9db6e3")
# Disabling resizing of the main window
root.resizable(False, False)

# Adding a label for the title of the application
Label(root, font=("Comic Sans MS", 16), text='Python Mad Libs Generator', background="#9db6e3").place(x=45, y=8)
# Adding a label for the subtitle
Label(root, font=("Comic Sans MS", 16), text='Have fun!', background="#9db6e3").place(x=130, y=35)

# Adding a button that starts the first Mad Libs game
ml1 = Button(root, text='The Gold', font=("Comic Sans MS", 16), command=lambda: first_madlib(root), bg='LightSkyBlue')
ml1.place(x=125, y=150)

# First Mad Lib - titled "The Gold"
def first_madlib(win):
    def finish_madlib(tl: Toplevel, animal, parent, month, path, movement, num):
        # Generating the final story based on user input
        text = f'''
There was once a {animal}. He was always getting told off. One day while his {parent} was sitting in the garden in {month}, he sneaked out. He did not mean to go far but he saw a glittery thing on the {path} and {movement} over to it. He found out it was gold and became rich because he had {num} pieces of gold.'''

        # Setting the dimensions of the new window to display the final story
        tl.geometry(newGeometry='375x550')

        # Displaying the final story in the new window
        Label(tl, text='Your Story:', font=("Times", 13, 'bold'), background='Gold', wraplength=tl.winfo_width()).place(x=130, y=310)
        Label(tl, text=text, font=("Times", 13), background='Gold', wraplength=tl.winfo_width()).place(x=0, y=330)

    # Creating the top level widget for the first Mad Libs game
    ml1_wn = Toplevel(win, bg='Gold')
    ml1_wn.title("The Gold")
    ml1_wn.geometry('375x500')
    ml1_wn.resizable(False, False)

    # Creating labels for the user prompts
    Label(ml1_wn, text='The Gold - Mad Libs', font=("Helvetica", 20, 'bold'), bg='Gold').place(x=60, y=0)
    Label(ml1_wn, text='An animal:', font=("Times", 15), bg='Gold').place(x=0, y=35)
    Label(ml1_wn, text='Choose a parent:', font=("Times", 15), bg='Gold').place(x=0, y=70)
    Label(ml1_wn, text='Choose a month:', font=("Times", 15), bg='Gold').place(x=0, y=110)
    Label(ml1_wn, text='Choose a path:', font=("Times", 15), bg='Gold').place(x=0, y=150)
    Label(ml1_wn, text='Choose a movement type:', font=("Times", 15), bg='Gold').place(x=0, y=190)
    Label(ml1_wn, text='A number:', font=("Times", 15), bg='Gold').place(x=0, y=230)

    # Creating the text input boxes for user input
    animal_entry = Entry(ml1_wn, width=17)
    animal_entry.place(x=250, y=35)
    num_entry = Entry(ml1_wn, width=17)
    num_entry.place(x=250, y=230)

    # Creating option menus for user to choose from predefined options
    parents = ['Mum', "Dad"]
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    movements = ['walked', 'ran']
    paths = ['grass', 'concrete']

    # Setting up the option menus with default values
    parent_opt = StringVar(ml1_wn)
    parent_opt.set(parents[0])
    OptionMenu(ml1_wn, parent_opt, *parents).place(x=270, y=70)

    month_opt = StringVar(ml1_wn)
    month_opt.set(months[0])
    OptionMenu(ml1_wn, month_opt, *months).place(x=255, y=110)

    path_opt = StringVar(ml1_wn)
    path_opt.set(paths[0])
    OptionMenu(ml1_wn, path_opt, *paths).place(x=270, y=150)

    movement_opt = StringVar(ml1_wn)
    movement_opt.set(movements[0])
    OptionMenu(ml1_wn, movement_opt, *movements).place(x=265, y=190)

    # Creating a 'Submit' button to generate the final story
    submit_btn = Button(ml1_wn, text="Submit", background="SteelBlue", font=('Times', 12), 
                        command=lambda: finish_madlib(ml1_wn, animal_entry.get(), parent_opt.get(), month_opt.get(), path_opt.get(), movement_opt.get(), num_entry.get()))
    submit_btn.place(x=150, y=270)

    # Running the main loop of the new window
    ml1_wn.mainloop()
    # Updating the main window
    root.update()

# Running the main loop of the application
root.mainloop()
