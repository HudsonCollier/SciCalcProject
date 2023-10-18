from tkinter import *
from tkinter import messagebox
from math import *
from random import randint
from math import sin, cos, tan, radians
from functools import wraps

# data in entry box
def entryBox(k):
    input_text = input_var.get()  
    if input_text == 'ERROR':
        entry_box.delete(0, END)  
    entry_box.config(fg='white')  
    entry_box.insert(END, k)  


# evaluate ...
def Evaluate(k):
    s = input_var.get()
    try:
        result = round(my_eval(s), 5)
        input_var.set(result)
    except:
        entry_box.config(fg='red')
        input_var.set("ERROR")


def my_eval(expr):
    expr = expr.replace('^', '**')
    return eval(expr)


def evaluate_trig_functions(s):      # the argument is converted from degrees to radians and is then evaluated using the corresponding trig function
    functions = {'sin(': sin, 'cos(': cos, 'tan(': tan}
    for func in functions:
        while func in s:
            start_index = s.index(func)
            end_index = start_index + len(func)
            arg_end_index = s.index(')', end_index)
            arg = int(s[end_index:arg_end_index])
            result = functions[func](radians(arg))
            s = s[:start_index] + str(result) + s[arg_end_index+1:]
    return s

def replace_inverse_trig_functions(s):     # this function replaces the sin-1 with a
    s = s.replace('sin-1', 'asin')
    s = s.replace('cos-1', 'acos')
    s = s.replace('tan-1', 'atan')
    return s

def my_evaluate(s):
    s = evaluate_trig_functions(s)
    s = replace_inverse_trig_functions(s)
    return s


def handle_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            entry_box.config(fg='red')
            input_var.set("ERROR")
    return wrapper

@handle_error
def SciEval(k):
    s = input_var.get()
    s = my_evaluate(s)
    result = eval(s)
    result = round(result, 5)
    input_var.set(result)


# clears the entry box
def clickCE():
    entry_box.delete(0,END)


# swaps the sign of the number in the entry box
def sign_switch():
    s = input_var.get()
    entry_box.delete(0, 'end')
    entry_box.insert(0, -float(s) if s and s[0] != '-' else abs(float(s)))


def Scientific():

    def squared(p):
        s = input_var.get()
        if not s.isnumeric() and not (s.startswith('-') and s[1:].isnumeric()):
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        s = float(s)
        result = round(pow(s, p), 5)
        input_var.set(result)


    def epower(pie):
        s = input_var.get()
        if not s.isnumeric() and not (s.startswith('-') and s[1:].isnumeric()):               
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        s = float(s)
        result = round(pow(pie, s), 5)
        input_var.set(result)


    def spower(k):
        s = input_var.get()
        if not s.isnumeric() and not (s.startswith('-') and s[1:].isnumeric()):        
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        s = float(s)
        result = round(pow(s, k), 5)
        input_var.set(result)


    def reciprocal():
        s = input_var.get()
        if not s.isnumeric() and not (s.startswith('-') and s[1:].isnumeric()):
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        s = float(s)
        if s == 0:
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        result = round(1 / s, 5)
        input_var.set(result)


    def calculate_factorial():
        s = input_var.get()
        if not s.isnumeric() and not (s.startswith('-') and s[1:].isnumeric()):
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        s = int(s)
        if s < 0:
            input_var.set("ERROR")
            entry_box.config(fg='red')
            return
        result = 1
        for i in range(1, s + 1):
            result *= i
            input_var.set(result)


    def random():
        entry_box.delete(0, END)
        input_var.set(str(randint(1,10000000000)))

    w.destroy()
    global entry_box
    global input_var
    w1=Tk()



    # Scientific Calculator
    w1.title("Scientific Calculator")
    w1.geometry("+300+300")
    w1.resizable(width=False, height=False)
    
    root = Frame(w1)
    input_var = StringVar()
    entry_box = Entry(root, width=50, textvariable=input_var, fg='white')
    entry_box.grid(row=0, column=0, columnspan=9)
    w1.propagate(0)

    squared_button = Button(root, text="x^2", width=5,fg='black', height=3, command=lambda :squared(2)).grid(row=1, column=0)
    two_root_button = Button(root, text="2√x", width=5, height=3, fg='black', command=lambda:spower(1/2)).grid(row=1,column=1)
    open_parentheses_button = Button(root, text="(", width=5, height=3, fg='black', command=lambda: entryBox("(")).grid(row=1, column=2)
    closed_parentheses_button = Button(root, text=")", width=5, height=3, fg='black', command=lambda: entryBox(")")).grid(row=1, column=3)
    pi_button = Button(root, text="π", width=5, height=3, fg='black',command=lambda: entryBox("3.1415926")).grid(row=1, column=4)
    clear_button = Button(root, text="CE", width=5, height=3, fg='black', command=clickCE).grid(row=1, column=5)
    switch_button = Button(root, text="-/+", width=5, height=3, fg='black', command=sign_switch).grid(row=1, column=6)
    modulo_button = Button(root, text="%", width=5, height=3, fg='black', command=lambda: entryBox("%")).grid(row=1, column=7)
    divide_button = Button(root, text="/", width=5, height=3, fg='black', command=lambda: entryBox("/")).grid(row=1, column=8)

    cuberoot_button = Button(root, text="x^3", width=5,fg='black', height=3, command=lambda :squared(3)).grid(row=2, column=0)
    three_root_button = Button(root, text="3√x", width=5, height=3, fg='black', command=lambda:spower(1/3)).grid(row=2,column=1)
    sin_button = Button(root, text="sin", width=5, height=3,fg='black', command=lambda: entryBox("sin(")).grid(row=2, column=2)
    inv_sin_button = Button(root, text="sin-1", width=5, height=3,fg='black', command=lambda: entryBox("sin-1(")).grid(row=2, column=3)
    sinh_button = Button(root, text="sinh", width=5, height=3,fg='black', command=lambda: entryBox("sinh(")).grid(row=2, column=4)
    button1 = Button(root, text="1", width=5, height=3, command=lambda: entryBox("1")).grid(row=2, column=5)
    button2 = Button(root, text="2", width=5, height=3, command=lambda: entryBox("2")).grid(row=2, column=6)
    button3 = Button(root, text="3", width=5, height=3, command=lambda: entryBox("3")).grid(row=2, column=7)
    plus_button = Button(root, text="+", width=5, height=3, fg='black', command=lambda: entryBox("+")).grid(row=2, column=8)
    
    ex_button = Button(root, text="e^x", width=5,fg='black', height=3, command=lambda :epower(2.718281828459045)).grid(row=3, column=0)
    one_over_x_button = Button(root, text="1/x", width=5, height=3,fg='black', command=reciprocal).grid(row=3, column=1)
    cos_button = Button(root, text="cos", width=5, height=3,fg='black', command=lambda: entryBox("cos(")).grid(row=3, column=2)
    inv_cos_button = Button(root, text="cos-1", width=5, height=3,fg='black', command=lambda: entryBox("cos-1(")).grid(row=3, column=3)
    cosh_button = Button(root, text="cosh", width=5, height=3,fg='black', command=lambda: entryBox("cosh")).grid(row=3, column=4)
    button4 = Button(root, text="4", width=5, height=3, command=lambda: entryBox("4")).grid(row=3, column=5)
    button5 = Button(root, text="5", width=5, height=3, command=lambda: entryBox("5")).grid(row=3, column=6)
    button6 = Button(root, text="6", width=5, height=3, command=lambda: entryBox("6")).grid(row=3, column=7)
    minus_button = Button(root, text="-", width=5, height=3, fg='black', command=lambda: entryBox("-")).grid(row=3, column=8)

    tenx_button = Button(root, text="10^x", width=5, height=3, fg='black', command=lambda :epower(10)).grid(row=4,column=0)
    xfactorial_button = Button(root, text="x!", width=5, height=3,fg='black', command=calculate_factorial).grid(row=4, column=1)
    tan_button = Button(root, text="tan", width=5, height=3, fg='black', command=lambda: entryBox("tan(")).grid(row=4, column=2)
    inv_tan_button = Button(root, text="tan-1", width=5, height=3, fg='black', command=lambda: entryBox("tan-1(")).grid(row=4,column=3)
    tanh_button = Button(root, text="tanh", width=5, height=3, fg='black', command=lambda: entryBox("tanh")).grid(row=4, column=4)
    button7 = Button(root, text="7", width=5, height=3, command=lambda: entryBox("7")).grid(row=4, column=5)
    button8 = Button(root, text="8", width=5, height=3, command=lambda: entryBox("8")).grid(row=4, column=6)
    button9 = Button(root, text="9", width=5, height=3, command=lambda: entryBox("9")).grid(row=4, column=7)
    multiplication_button = Button(root, text="*", width=5, height=3, fg='black', command=lambda: entryBox("*")).grid(row=4, column=8)
    
    twox_button = Button(root, text="2^x", width=5, height=3, fg='black', command=lambda :epower(2)).grid(row=5,column=0)
    rand_button = Button(root, text="Rand", width=5, height=3,fg='black', command=random).grid(row=5, column=1)
    e_button = Button(root, text="e", width=5, height=3, fg='black', command=lambda: entryBox("2.71828182")).grid(row=5, column=2)
    logten_button = Button(root, text="log10", width=5, height=3, fg='black', command=lambda: entryBox("log10(")).grid(row=5,column=3)
    log_button = Button(root, text="log", width=5, height=3, fg='black', command=lambda: entryBox("log(")).grid(row=5, column=4)
    dot_button = Button(root, text=".", width=5, height=3, fg='black', command=lambda: entryBox(".")).grid(row=5, column=7)
    equal_button = Button(root, text="=", width=5, height=3, fg='black', command=lambda: SciEval(k)).grid(row=5, column=8)
    
    button0 = Button(root, text="0", width=10, height=3, command=lambda: entryBox("0")).grid(row=5, column=5, columnspan=2)
    
    k = None
    
    w1.bind("<Return>", SciEval)
    root.grid(row=0, column=0)
    w1.mainloop()




# Normal Calc
w=Tk()
main_menu=Menu(w)
w.config(menu=main_menu)
submenu1=Menu(main_menu)
submenu2=Menu(main_menu)
main_menu.add_cascade(label='View',menu=submenu1)
submenu1.add_command(label='Scientific',command=Scientific)
main_menu.add_cascade(label='Options',menu=submenu2)
submenu2.add_command(label='Help',command=None)
submenu2.add_command(label='Exit',command=quit)

w.title("Calculator")
w.geometry("+300+300")
w.resizable(width=False,height=False)
root=Frame(w)
input_var=StringVar()
entry_box=Entry(root,width=20,textvariable=input_var,fg='white')
entry_box.grid(row=0,column=0,columnspan=4)
w.propagate(0)

buttonce=Button(root,text="CE",width=5,height=3,fg='black',command=clickCE).grid(row=1,column=0)
switch_button=Button(root,text="+/-",width=5,height=3,fg='black',command=sign_switch).grid(row=1,column=1)
modulo_button=Button(root,text="%",width=5,height=3,fg='black',command=lambda :entryBox("%")).grid(row=1,column=2)
division_button=Button(root,text="/",width=5,height=3,fg='black',command=lambda :entryBox("/")).grid(row=1,column=3)

button1=Button(root,text="1",width=5,height=3,command=lambda :entryBox("1")).grid(row=2,column=0)
button2=Button(root,text="2",width=5,height=3,command=lambda :entryBox("2")).grid(row=2,column=1)
button3=Button(root,text="3",width=5,height=3,command=lambda :entryBox("3")).grid(row=2,column=2)
plus_button=Button(root,text="+",width=5,height=3,fg='black',command=lambda :entryBox("+")).grid(row=2,column=3)

button4=Button(root,text="4",width=5,height=3,command=lambda :entryBox("4")).grid(row=3,column=0)
button5=Button(root,text="5",width=5,height=3,command=lambda :entryBox("5")).grid(row=3,column=1)
button6=Button(root,text="6",width=5,height=3,command=lambda :entryBox("6")).grid(row=3,column=2)
minus_button=Button(root,text="-",width=5,height=3,fg='black',command=lambda :entryBox("-")).grid(row=3,column=3)

button7=Button(root,text="7",width=5,height=3,command=lambda :entryBox("7")).grid(row=4,column=0)
button8=Button(root,text="8",width=5,height=3,command=lambda :entryBox("8")).grid(row=4,column=1)
button9=Button(root,text="9",width=5,height=3,command=lambda :entryBox("9")).grid(row=4,column=2)
multiplication_button=Button(root,text="*",width=5,height=3,fg='black',command=lambda :entryBox("*")).grid(row=4,column=3)

button0=Button(root,text="0",width=10,height=3,command=lambda :entryBox("0")).grid(row=5,column=0,columnspan=2)
dot_button=Button(root,text=".",width=5,height=3,fg='black',command=lambda :entryBox(".")).grid(row=5,column=2)
k=None
equal_button=Button(root,text="=",width=5,height=3,fg='black',command=lambda :Evaluate(k)).grid(row=5,column=3)

w.bind("<Return>",Evaluate)
root.grid(row=0,column=0)
w.mainloop()