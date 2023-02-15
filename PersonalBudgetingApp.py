from tkinter import *
from tkinter import ttk
import datetime
import sqlite3

def connect():
    con = sqlite3.connect("personalbudget.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Buget(Month, IncomeAmt, TotalExpense, BugetAmt)")
    cur.close()
    con.commit()
    con.close()

def View():

    con1 = sqlite3.connect("personalbudget.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM Buget")

    rows = cur1.fetchall()    

    for row in rows:

        print(row) 

        tree.insert(parent= "", index= "end" ,values=row)        

    con1.close() 

def put():
    con2 = sqlite3.connect("personalbudget.db")
    cur2 = con2.cursor()
    cur2.execute("INSERT INTO Buget values('%s','%s','%s','%s')"%(month.get(), incomeStr.get(), expenseStr.get(), budgetStr.get()))
    cur2.close()
    con2.commit()
    con2.close()

root = Tk()

month = StringVar()
incomeStr = StringVar()
expenseStr = StringVar()
budgetStr = StringVar()


connect()

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
tree.heading("#1", text="Month")
tree.heading("#2", text="IncomeAmt")
tree.heading("#3", text="TotalExpense")
tree.heading("#4", text="BugetAmt")
tree.grid()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Enter the Month: ').grid(row= 0, column= 0)
ttk.Label(frm, text='Enter your Income: ').grid(row= 1, column= 0)
ttk.Label(frm, text='Enter your total Expense: ').grid(row= 2, column= 0)
ttk.Label(frm, text='Enter your Budget: ').grid(row= 3, column= 0)

ttk.Entry(frm, textvariable= month).grid(row= 0, column= 1)
ttk.Entry(frm, textvariable= incomeStr).grid(row= 1, column= 1)
ttk.Entry(frm, textvariable= expenseStr).grid(row= 2, column= 1)
ttk.Entry(frm, textvariable= budgetStr).grid(row= 3, column= 1)

ttk.Button(frm, text='Submit', command= put).grid(row= 4, column= 0)
ttk.Button(frm, text='View Data', command= View).grid(row= 4, column= 1)
ttk.Button(frm, text='Exit').grid(row= 4, column= 2)



root.mainloop()