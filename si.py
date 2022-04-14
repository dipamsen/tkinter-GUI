from tkinter import *

window = Tk()
window.configure(bg="lightgreen", width=400, height=400)
window.title("Interest Calculator")


def create_label_entry(fieldname):
    label = Label(window, text="Enter {}".format(fieldname),
                  bg="lightgreen", font=(fontname, 14))
    entry = Entry(window, text="")
    return label, entry


def calculate_interest():
    p = float(principal_e.get())
    t = float(time_e.get())
    r = float(rate_e.get())
    interest = p*t*r/100
    result_box.configure(text="Interest Amount = {}".format(str(interest)))


fontname = "Comic Sans MS"

title_l = Label(text="Simple Interest Calculator",
                font=(fontname, 20), bg="lightgreen")
title_l.place(relx=0, rely=0.05, relwidth=1)

principal_l, principal_e = create_label_entry("Principal Amount (Rs)")
principal_l.place(relx=0.05, rely=0.2)
principal_e.place(relx=0.2, rely=0.28, relwidth=0.6)

rate_l, rate_e = create_label_entry("Rate of Interest (% per annum)")
rate_l.place(relx=0.05, rely=0.36)
rate_e.place(relx=0.2, rely=0.44, relwidth=0.6)

time_l, time_e = create_label_entry("Interest Duration (years)")
time_l.place(relx=0.05, rely=0.52)
time_e.place(relx=0.2, rely=0.6, relwidth=0.6)

calculate_btn = Button(window, text="Calculate", font=(
    fontname, 16), bg="blue", fg="white", command=calculate_interest)
calculate_btn.place(rely=0.7, x=100, relwidth=0.5)


result_box = Label(window, text="", font=(
    fontname, 14), bg="green", fg="white")
result_box.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.85)


window.mainloop()
