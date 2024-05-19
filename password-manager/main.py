import json
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatePassword():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(3, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    generated_password = "".join(password_list)
    pass_entry.delete(0, "end")
    pass_entry.insert(0,generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    password_data = { website:{
        "username": username,
        "password": password,
    },

    }
    if website == "" or username=="" or password=="":
        messagebox.showerror(title="Error", message="Please Don't leave any field empty!")
        return
    is_ok = messagebox.askokcancel(title=website,message=f"Details entered \nemail/username: {username}\n"
                                                 f"password: {password}\nis it ok to save?")

    if is_ok:
        #to catch exception as it will produce error because we are reading empty json file
        try:
            with open("data.json",mode="r") as file:
                #to update data in dictionary

                #reading old data
                data = json.load(file)
                #updating old data with new data
                data.update(password_data)

        #appending data
        except:
            with open("data.json", mode="w") as file:
                json.dump(password_data,file,indent=4)



        else:
            with open("data.json", mode="w") as file:
                json.dump(data,file,indent=4)
        finally:
            web_entry.delete(0, "end")
            user_entry.delete(0, "end")
            pass_entry.delete(0, "end")
            web_entry.focus()
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
        web = data[website]

        if website in data:
            messagebox.showinfo(title="password",message=f"Email:{web["username"]} \n Password {web["password"]}")
    except KeyError:
        messagebox.showerror(title="error",message=f"password not found for {website}")

    except:
        messagebox.showerror(title="error",message="No file found, first add website")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("password generator")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)

canvas.grid(row=1,column=2)

website = Label(text="Website: ")
website.grid(row=2,column=1)

web_entry = Entry(width=35)
web_entry.grid(row=2,column = 2,columnspan = 2)
web_entry.focus()

email = Label(text="Email/Username: ")
email.grid(row=3,column=1)

user_entry = Entry(width=35)
user_entry.grid(row=3,column = 2,columnspan = 2)

password = Label(text="Password")
password.grid(row=4,column=1)

pass_entry = Entry(width = 17)
pass_entry.grid(row=4,column=2)


generate = Button(text="Generate Password",command=generatePassword)
generate.grid(row=4,column=3)


add_button =Button(text="ADD",width=36,command=add)
add_button.grid(row=5,column=2,columnspan = 2)

search_button = Button(text="Search",width=10,command=search)
search_button.grid(row=2 , column= 3)



window.mainloop()