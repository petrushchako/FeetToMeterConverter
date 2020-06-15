from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background = "azure")
window.geometry("320x220")
window.resizable(width=False, height=False)

def convert():
    if mt_entry.get() == "":
        value = float(ft_entry.get()) #.get() to get vallue from ft_entry Entry widget
        meter = value * 0.3048
        mt_value.set("%.4f" % meter) #set() value of Meter widget. "%.4f" floating point number with 4 numbers decimal percision
    elif ft_entry.get() == "":
        value = float(mt_entry.get())
        feet = value * 3.28084
        ft_value.set("%.4f" % feet)
    else:
        return #can't use break in if statement


def clear():
    ft_value.set("")
    mt_value.set("")


#Feet Label
ft_lbl = Label(window, text="Feet", bg="dark orchid", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)
#Feet Entry window with DoubleVar data type
ft_value = DoubleVar()
ft_entry = Entry(window, textvariable = ft_value, width = 25)
ft_entry.grid(column=1, row=0, padx=15, pady=15)
ft_entry.delete(0, 'end')

#Meter Label
mt_lbl=Label(window, text="Meter", bg="RoyalBlue1", fg="white", width=14)
mt_lbl.grid(column=0, row=1, padx=15, pady=15)
#Meter Entry window with DoubleVar data type
mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=25)
mt_entry.grid(column=1,row=1, pady=30)
mt_entry.delete(0, 'end')

#Convert Button
convert_btn=Button(window, text="Convert", bg="green4", fg="white", width=14, command=convert)
convert_btn.grid(column=0, row=3, pady=30)

#Clear Button
clear_btn=Button(window, text="Clear", bg="firebrick1", fg="white", width=14, command=clear)
clear_btn.grid(column=1, row=3, pady=30)

window.mainloop()
