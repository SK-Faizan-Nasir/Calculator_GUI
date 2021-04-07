from tkinter import *
from tkinter import messagebox
root = Tk()
def author():
    messagebox.showinfo("Author","SK Faizan Nasir")
def button_click(number):
    current = display.get()
    display.delete(0,END)
    display.insert(0,str(current)+str(number))

def button_clear():
    display.delete(0,END)

def button_add():
    first_number = display.get()
    global  f_num
    global math
    math = "add"
    f_num = int(first_number)
    display.delete(0,END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    display.delete(0, END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    display.delete(0, END)

def button_divide():
    first_number = display.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    display.delete(0, END)

def button_equal():
    second_number = display.get()
    display.delete(0,END)
    if math == "add":
        display.insert(0, f_num + int(second_number))
    elif math == "subtract":
        display.insert(0, f_num - int(second_number))
    elif math == "multiply":
        display.insert(0, f_num * int(second_number))
    elif math=="divide":
        display.insert(0, f_num / int(second_number))

display = Entry(root,width = 45,border = 6)
display.grid(row = 0, column =0,columnspan = 3,padx=10,pady=10)
button1 = Button(root, text = "1",padx=40,pady=20,command = lambda : button_click(1) )
button1.grid(row = 1, column = 0)
button2 = Button(root, text = "2",padx=40,pady=20,command = lambda : button_click(2) )
button2.grid(row = 1,column = 1)
button3 = Button(root, text = "3",padx=40,pady=20,command = lambda : button_click(3) )
button3.grid(row=1,column = 2)
button4 = Button(root, text = "4",padx=40,pady=20,command = lambda : button_click(4) )
button4.grid(row=2,column=0)
button5 = Button(root, text = "5",padx=40,pady=20,command = lambda : button_click(5) )
button5.grid(row=2,column=1)
button6 = Button(root, text = "6",padx=40,pady=20,command = lambda : button_click(6) )
button6.grid(row=2,column=2)
button7 = Button(root, text = "7",padx=40,pady=20,command = lambda : button_click(7) )
button7.grid(row=3,column = 0)
button8 = Button(root, text = "8",padx=40,pady=20,command = lambda : button_click(8) )
button8.grid(row=3,column=1)
button9 = Button(root, text = "9",padx=40,pady=20,command = lambda : button_click(9) )
button9.grid(row=3,column=2)
button0 = Button(root, text = "0",padx=40,pady=20,command = lambda : button_click(0) )
button0.grid(row=4,column=0)
button_add = Button(root, text = "+" ,padx=89,pady=20,command = button_add)
button_add.grid(row=4,column=1,columnspan=2)
button_substaract = Button(root,text ="-    ",padx = 40,pady = 20, command =button_subtract)
button_substaract.grid(row = 5,column = 0)
button_multiply = Button(root,text = "*     ",padx= 40,pady = 20,command = button_multiply)
button_multiply.grid(row = 5 ,column = 1)
button_divide  =Button(root,text = "/ ",padx = 38,pady = 20,command = button_divide)
button_divide.grid(row = 5,column =2)
button_equal = Button(root, text = "=     ",padx=132,command = button_equal)
button_equal.grid(row=6,column=0,columnspan = 3)
button_clear = Button(root, text = "Clear",padx=130,command = button_clear)
button_clear.grid(row=7,column=0,columnspan = 3)
button_author = Button(root,text = "Author",padx = 125,command = author)
button_author.grid(row=8,column = 0, columnspan = 3)


root.mainloop()
