from tkinter import *
from password import Password
import pickle

try:
    pickle_in = open("pass_dict.pickle", "rb")
    password_dict = pickle.load(pickle_in)
except FileNotFoundError:
    password_dict = {}

try:
    print(password_dict["Facebook"])
except KeyError:
    print("password not found")

window = Tk()
window.title('Password Manager')
# window.geometry("400x250")


def gen_password():
    generated_pass.set(
        Password.generate_password(pass_len.get(), digits.get(), lowercase.get(), uppercase.get(), symbols.get()))


def copy():
    window.clipboard_clear()
    window.clipboard_append(generated_pass.get())


def save(passname):
    pass_name = Password(entry_name.get(), entry_username.get(), entry_password.get(), entry_website.get())
    print(pass_name)
    password_dict[passname] = pass_name
    pickle_out = open("pass_dict.pickle", "wb")
    pickle.dump(password_dict, pickle_out)
    pickle_out.close()


def pass_strength(scale_var):
    if (
            digits.get() * 10 + lowercase.get() * 26 + uppercase.get() * 26 + symbols.get() * 14) ** pass_len.get() < 10 ** 16:
        pass_str.set("Weak")
    elif (
            digits.get() * 10 + lowercase.get() * 26 + uppercase.get() * 26 + symbols.get() * 14) ** pass_len.get() < 10 ** 23:
        pass_str.set("Medium")
    elif (
            digits.get() * 10 + lowercase.get() * 26 + uppercase.get() * 26 + symbols.get() * 14) ** pass_len.get() < 10 ** 26:
        pass_str.set("Strong")
    else:
        pass_str.set("Very Strong")


digits = IntVar()
lowercase = IntVar()
uppercase = IntVar()
symbols = IntVar()
pass_len = IntVar()
generated_pass = StringVar()
pass_str = StringVar()

btn_generate = Button(window, text='Generate', width=6, command=gen_password)
btn_generate.grid(row=5, column=1)
btn_copy = Button(window, text='Copy', width=6, command=copy)
btn_copy.grid(row=5, column=2)
btn_save = Button(window, text='Save Password', width=11, command=lambda: save(entry_name.get()))
btn_save.grid(row=3, column=2)

scale_len = Scale(window, from_=6, to=20, orient=HORIZONTAL, variable=pass_len, command=pass_strength)
scale_len.grid(row=7, column=1)

btn_digits = Checkbutton(window, text='Digits', variable=digits, onvalue=1, offvalue=0,
                         command=lambda: pass_strength(''))
btn_digits.grid(row=4, column=0, sticky=W)
btn_lowercase = Checkbutton(window, text='Lowercase Letters', variable=lowercase, onvalue=1, offvalue=0,
                            command=lambda: pass_strength(''))
btn_lowercase.grid(row=5, column=0, sticky=W)
btn_uppercase = Checkbutton(window, text='Uppercase Letters', variable=uppercase, onvalue=1, offvalue=0,
                            command=lambda: pass_strength(''))
btn_uppercase.grid(row=6, column=0, sticky=W)
btn_symbols = Checkbutton(window, text='Symbols', variable=symbols, onvalue=1, offvalue=0,
                          command=lambda: pass_strength(''))
btn_symbols.grid(row=7, column=0, sticky=W)

label_pass = Label(window, textvariable=generated_pass, relief=SUNKEN, width=24)
label_pass.grid(row=6, column=1)

label_name = Label(window, text="Name:")
label_name.grid(row=0, column=0, sticky=W)
entry_name = Entry(window)
entry_name.grid(row=0, column=1)

label_username = Label(window, text="Username:")
label_username.grid(row=1, column=0, sticky=W)
entry_username = Entry(window)
entry_username.grid(row=1, column=1)

label_password = Label(window, text="Password:")
label_password.grid(row=2, column=0, sticky=W)
entry_password = Entry(window)
entry_password.grid(row=2, column=1)

label_website = Label(window, text="Website:")
label_website.grid(row=3, column=0, sticky=W)
entry_website = Entry(window)
entry_website.grid(row=3, column=1)

label_str = Label(window, text="Strength:")
label_str.grid(row=8, column=0, sticky=W)
label_str_ind = Label(window, textvariable=pass_str)
label_str_ind.grid(row=8, column=1)

window.mainloop()
