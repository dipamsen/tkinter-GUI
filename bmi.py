from tkinter import *

window = Tk()

window.title("BMI Calculator")
window.geometry("380x400")
window.configure(bg="lightblue")


def calculate_bmi():
    global result_label
    weight = int(weight_entry.get())
    height = int(height_entry.get()) / 100
    bmi = weight / (height * height)
    bmi = round(bmi, 1)
    name = username.get()
    result_label.destroy()
    message = ""
    bgcolor = "white"
    if bmi <= 18.5:
        message = "You are underweight."
        bgcolor = "yellow"
    elif bmi > 18.5 and bmi <= 25:
        message = "Normal Range."
        bgcolor = "lightgreen"
    elif bmi > 25 and bmi <= 30:
        message = "You are overweight."
        bgcolor = "pink"
    elif bmi > 30:
        message = "You are obese."
        bgcolor = "pink"
    else:
        message = "Something went wrong."

    result_label = Label(result_frame, text="{}, Your BMI is {}. {}".format(
        name, str(bmi), message), bg=bgcolor, width=40)
    result_label.place(x=20, y=40)
    result_label.pack()


heading_label = Label(window, text="BMI Calculator",
                      fg="black", bg="lightblue", font=("Arial", 20), bd=5)
heading_label.place(x=50, y=20)

name_label = Label(window, text="Your Name", fg="darkblue",
                   bg="lightblue", font=("Arial", 16), bd=1)
name_label.place(x=20, y=90)

username = Entry(window, text="", bd=2, width=20)
username.place(x=150, y=92)

height_label = Label(window, text="Enter Height (cm)",
                     fg="black", bg="lightblue", font=("Arial", 14))
height_label.place(x=20, y=140)

height_entry = Entry(window, text="", bd=2, width=50)
height_entry.place(x=180, y=140)

weight_label = Label(window, text="Enter Weight (kg)",
                     fg="black", bg="lightblue", font=("Arial", 14))
weight_label.place(x=20, y=185)

weight_entry = Entry(window, text="", bd=2, width=50)
weight_entry.place(x=180, y=185)

calc_button = Button(window, text="Calculate", fg="white",
                     bg="blue", bd=4, command=calculate_bmi)
calc_button.place(x=120, y=255)

result_frame = LabelFrame(window, text="Result",
                          bg="lightgrey", font=("Arial", 20))
result_frame.pack(padx=20, pady=30)
result_frame.place(x=20, y=300)

result_label = Label(result_frame, text="", bg="lightgrey",
                     font=("Arial", 20), width=20)
result_label.place(x=20, y=20)
result_label.pack()


window.mainloop()
