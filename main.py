from tkinter import *

window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30,pady=30)

def miles_to_km():
    miles=float(miles_input.get())
    km=miles*1.609
    km_result_label.config(text=f"{km}")

miles_input=Entry(width=7)
miles_input.grid(column=2,row=1)

miles_lable=Label(text="Miles")
miles_lable.grid(column=3,row=1)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=1,row=2)

km_result_label=Label(text="0")
km_result_label.grid(column=2,row=2)

km_label=Label(text="Km")
km_label.grid(column=3,row=2)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=2,row=3)



window.mainloop()