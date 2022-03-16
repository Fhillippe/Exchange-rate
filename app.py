from tkinter import*
from Exchange_rate import*
from tkinter import messagebox


def task(self):
    global rate,number1,number2
    
    keyA = currency_list.index(valueA.get())
    keyB = currency_list.index(valueB.get())

    
    
    rate = exchange_rate(currency_keys[keyA],currency_keys[keyB])

    number1=0
    number2=0

    root.after(2000, calculate)

def calculate():
    global rate,number1,number2

    
    try:
        if entryone.get()!=str(number1):
            
            number1 = entryone.get()
            entrytwo.delete(0,END)
            if entryone.get():
                number2 = round(float(entryone.get())*float(rate),2)
            entrytwo.insert(0,str(number2))

        elif  entrytwo.get()!=str(number2):
            number2 = entrytwo.get()
            entryone.delete(0,END)
            if entrytwo.get():
                number1 = round(float(entrytwo.get())/float(rate),2)
            entryone.insert(0,str(number1))
    except ValueError:
        entryone.delete(0,END)
        entrytwo.delete(0,END)
        entryone.insert(0,''.join([x for x in str(number1) if (x >='0' and x<='9') or x=='.']))
        entrytwo.insert(0,''.join([x for x in str(number2) if (x >='0' and x<='9') or x=='.']))
        messagebox.showerror('Bad imput','Bad imput')

    root.after(50, calculate)


def get_key(value):
    return currency_keys[currency_list.index(value.get())]




root = Tk()
root.geometry("400x400")

entryone = Entry(root)
entrytwo = Entry(root)

entryone.insert(0,"0")
entrytwo.insert(0,"0")

    
entryone.grid(row = 0,column = 0)
entrytwo.grid(row = 1,column = 0)



currency_dict = currency_list()
currency_list = list(currency_dict.values())
currency_keys = [x for x,y in currency_dict.items()]
sorted_list = currency_list.copy()
sorted_list.sort()



valueA = StringVar()
valueA.set(sorted_list[0])

valueB = StringVar()
valueB.set(sorted_list[1])


dropOne = OptionMenu(root,valueA,*sorted_list,command=task)
dropTwo = OptionMenu(root,valueB,*sorted_list,command=task)

dropOne.grid(row=0, column=1)
dropTwo.grid(row=1, column=1)
  




    

root.mainloop()
