import customtkinter
from tkinter import messagebox
import webbrowser


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def convert_temperature():

    if celsius_entry.get() == "" and fahrenheit_entry.get() == "":
        messagebox.showinfo("Atention!", "Please enter a temperature")

    if celsius_entry.get() != "":
        celsius = float(celsius_entry.get())
        transform = round(celsius_to_fahrenheit(celsius), 5)
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", f"{celsius} C = {transform} F")

    if fahrenheit_entry.get() != "":
        f = float(fahrenheit_entry.get())
        transform = round(fahrenheit_to_celsius(f), 5)
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", f"{f} F = {transform} C")

        if celsius_entry.get() != "" and fahrenheit_entry.get() != "":
            celsius = float(celsius_entry.get())
            transform_c_to_f = round(celsius_to_fahrenheit(celsius), 5)

            f = float(fahrenheit_entry.get())
            transform_f_to_c = round(fahrenheit_to_celsius(f), 5)

            textbox.configure(state="normal")
            textbox.delete("1.0", "end")
            textbox.insert("1.0", f"{celsius} C = {transform_c_to_f} F\n\n\n")
            textbox.insert("2.0", f"{f} F = {transform_f_to_c} C")


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def convert_distance():

    if km_entry.get() == "" and mile_entry.get() == "":
        messagebox.showinfo("Attention!", "Please enter a distance")

    if km_entry.get() != "":
        km = float(km_entry.get())
        transform = round(km_to_miles(km), 4)
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", f"{km} km = {transform} miles")

    if mile_entry.get() != "":
        miles = float(mile_entry.get())
        transform = round(miles_to_km(miles), 4)
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", f"{miles} miles = {transform} km")

    if km_entry.get() != "" and mile_entry.get() != "":
        km = float(km_entry.get())
        transform_c_to_f = round(km_to_miles(km), 4)

        miles = float(mile_entry.get())
        transform_f_to_c = round(miles_to_km(miles), 4)

        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", f"{km} km = {transform_c_to_f} miles\n\n\n")
        textbox.insert("2.0", f"{miles} miles = {transform_f_to_c} km")


root = customtkinter.CTk()
root.geometry("720x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

font = ("Times", 24)
fontt = ("Times", 30)
font2 = ("Arial", 20, "italic")
label = customtkinter.CTkLabel(master=frame, text="Convertor", font=fontt)
label.pack(pady=12, padx=10)


celsius_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Celsius", font=font)
fahrenheit_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Fahrenheit", font=font)
km_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Kilometers", font=font)
mile_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Miles", font=font)


def optionmenu_callback(choice):
    # print("optionmenu dropdown clicked:", choice)
    textbox.delete("1.0", "end")
    if choice == "Temperature":
        km_entry.place_forget()
        mile_entry.place_forget()
        celsius_entry.place(x=100, y=130)
        fahrenheit_entry.place(x=100, y=180)
        button = customtkinter.CTkButton(master=frame, text="Convert", command=convert_temperature)
    else:
        celsius_entry.place_forget()
        fahrenheit_entry.place_forget()
        km_entry.place(x=100, y=130)
        mile_entry.place(x=100, y=180)
        button = customtkinter.CTkButton(master=frame, text="Convert", command=convert_distance)
    button.pack()
    button.place(x=250, y=160)
    textbox.place(x=100, y=250)


optionmenu_var = customtkinter.StringVar(value="Choose an option")

optionmenu = customtkinter.CTkOptionMenu(master=frame, values=["Temperature", "Distance"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var,
                                         font=font)


def open_insta():
    webbrowser.open("https://www.instagram.com/grozav_paul?igsh=c2F4NTFrZ3BsMWpp")


def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/paul-grozav-b39b0a2aa/")


def startupfcn():
    optionmenu.place(x=100, y=90)
    Start_button.destroy()
    label1.destroy()
    label2.destroy()
    label3.destroy()
    insta.destroy()
    linked_in.destroy()
    mail.destroy()


Start_button = customtkinter.CTkButton(master=frame, text="Start", command=startupfcn, font=font2)
label1 = customtkinter.CTkLabel(master=frame, text="Welcome to the Unit Converter!", font=font,)
label1.place(x=20, y=90)
label2 = customtkinter.CTkLabel(master=frame, text="Press the start button to begin.", font=font)
label2.place(x=20, y=130)
label3 = customtkinter.CTkLabel(master=frame, text="Contact me on: ", font=font)
label3.place(x=350, y=280)


insta = customtkinter.CTkButton(master=frame, text="Instagram - grozav_paul", command=open_insta, fg_color="#B02597")
insta.place(x=370, y=320)

linked_in = customtkinter.CTkButton(master=frame, text="LinkedIn", command=open_linkedin, fg_color="#1F69BE")
linked_in.place(x=370, y=360)

mail = customtkinter.CTkButton(master=frame, text="paulgrozav04@gmail.com", fg_color="#860909")
mail.place(x=370, y=400)

Start_button.place(x=225, y=200)


textbox = customtkinter.CTkTextbox(master=frame, font=font2, width=280, height=140)
textbox.configure(state="disabled")

root.mainloop()
