# Password Manager GUI v0.1
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    pass_ent.delete(0,END)
    # Create a variable named letters containing both lowercase and uppercase letters
    letters = list(string.ascii_lowercase + string.ascii_uppercase)

    # Create a variable named numbers containing numbers from 0 to 9
    numbers = list(map(str, range(10)))

    # Create a variable named symbols containing common symbols
    symbols = ['!','@','#','$','%','&','+','*','(',')']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)
    #print(f"Your password is: {pass_word}")
    pass_ent.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_ent.get()
    email = em_ent.get()
    pswd = pass_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": pswd,
        }
    }
    if len(website) == 0 or len(pswd) == 0:
        messagebox.showinfo(title="Oops", message="Please enter some value.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Update Old Data with New Data
            data.update(new_data)
        
            with open("data.json", "w") as data_file:
                #Saving Updated Data
                json.dump(data, data_file, indent=4)
        finally:
            web_ent.delete(0,END)
            pass_ent.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_json():
    website = web_ent.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No passwords data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"{website} - Data Does Not Exist.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("AKM Password Manager")
window.config(padx=30,pady=30)

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(120,120,image=logo)
canvas.grid(column=1,row=0)

#Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)

#Entry
web_ent = Entry(width=21)
web_ent.grid(row=1,column=1)
web_ent.focus()
em_ent = Entry(width=38)
em_ent.grid(column=1,row=2, columnspan=2)
em_ent.insert(0, "ak.muniswamy2023@gmail.com")
pass_ent = Entry(width=21)
pass_ent.grid(column=1,row=3)

#Buttons
search = Button(text="Search", width=13, command=find_json)
search.grid(row=1,column=2)
gen = Button(text="Generate Password",command=generate)
gen.grid(row=3, column=2)
add = Button(text="Add", width=36,command=save)
add.grid(row=4,column=1,columnspan=2)

############## DROP DOWN MENU #########################

def on_select(value):
    em_ent.delete(0, END)  # Clear the current text in the Entry
    em_ent.insert(0, value)  # Insert the selected value into the Entry

# Create a StringVar to store the selected value
selected_value = StringVar(window)

# Define the options for the dropdown menu
options = ["ak.muniswamy2023@gmail.com", "akumarm@ncsu.edu", 
           "ashwinkumar.m2014@gmail.com", "ashwinkumar.ak2020@gmail.com",
           "shakil.virgo.66@gmail.com","mmudaliar65@gmail.com",
           "aishlakshmi.93@gmail.com"]

# Set the default value
selected_value.set(options[0])

# Create the dropdown menu
dropdown_menu = OptionMenu(window, selected_value, command=on_select, *options)
dropdown_menu.grid(row=5, column=1)


window.mainloop()
# END OF CODE