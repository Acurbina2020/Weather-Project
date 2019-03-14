from tkinter import *
from tkinter import ttk
from sql_save import *
import sqlite3

db = "weather.db"
table = "temperature"
attrTypes = "(country TEXT, city TEXT, year INTEGER, high INTEGER, low INTEGER)"


createTable(db, table, attrTypes)


def saveToDB():
    countryVal = country.get()
    cityVal = city.get()
    yearVal = year.get()
    highVal = high.get()
    lowVal = low.get()
    insertData(db, table, (countryVal,cityVal,yearVal,highVal,lowVal))
    print(view(db,table))


def quit_msg():
    quit_window=Tk()
    frame1 = Frame(quit_window, highlightbackground="green", highlightcolor="green",highlightthickness=1, bd=0)
    frame1.pack()
    quit_window.overrideredirect(1)
    quit_window.geometry("200x70+650+400")
    lbl = Label(frame1, text="Are you sure you want to quit?")
    lbl.pack()
    yes_btn = Button(frame1, text="Yes", bg="light blue", fg="red",command=quit, width=10)
    yes_btn.pack(padx=10, pady=10 , side=LEFT)
    no_btn = Button(frame1, text="No", bg="light blue", fg="red",command=quit_window.destroy, width=10)
    no_btn.pack(padx=10, pady=10, side=LEFT)
    quit_window.mainloop()

window = Tk()

text1 = Text (window, bg = "yellow", fg = "black", width = 39, height = 1)
text1.insert(END, "Please enter the requested data")
text1.grid(row = 0, column = 0)

text2 = Text (window, bg = "black", fg = "white", width = 39, height = 1)
text2.insert(END, "Country:")
text2.grid(row = 1, column = 0)

country = StringVar()
countryName = Entry(window, textvariable = country, width = 30)
countryName.grid(row = 1, column = 1)

text3 = Text (window, bg = "black", fg = "white", width = 39, height = 1)
text3.insert(END, "City:")
text3.grid(row = 2, column = 0)

city = StringVar()
cityName = Entry(window, textvariable = city, width = 30)
cityName.grid(row = 2, column = 1)

text4 = Text (window, bg = "black", fg = "white", width = 39, height = 1)
text4.insert(END, "Year:")
text4.grid(row = 3, column = 0)

year = StringVar()
yearNum = Entry(window, textvariable = year, width = 30)
yearNum.grid(row = 3, column = 1)

text5 = Text (window, bg = "black", fg = "white", width = 39, height = 1)
text5.insert(END, "Max. Temperature (ºc):")
text5.grid(row = 4, column = 0)

high = StringVar()
highNum = Entry(window, textvariable = high, width = 30)
highNum.grid(row = 4, column = 1)

text6 = Text (window, bg = "black", fg = "white", width = 39, height = 1)
text6.insert(END, "Min. Temperature (ºc):")
text6.grid(row = 5, column = 0)

low = StringVar()
lowNum = Entry(window, textvariable = low, width = 30)
lowNum.grid(row = 5, column = 1)

text6 = Text (window, bg = "yellow", fg = "black", width = 39, height = 1)
text6.insert(END, "Or check existing data (e.g. 'Berlin'):")
text6.grid(row = 6, column = 0)

def showData():
    user_input = searchData.get()
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql_query = "SELECT country, year, high, low FROM temperature WHERE city = ?".format(table)
    cur.execute(sql_query, [user_input])
    rows = cur.fetchall()
    conn.close()
    return rows


def insert_rows():
    for row in showData():
        list1.insert(END, row)

def clear_rows():
    for row in showData():
        list1.delete(0, END)


list1 = Listbox(window, height=6,width=35)
list1.grid(row = 7, column = 0)

searchData = StringVar()
searchDataName = Entry(window, textvariable = searchData, width = 30)
searchDataName.grid(row = 6, column = 1)

viewData = Button(window, text = "View Data", command = lambda: insert_rows(), width = 8, height = 1, fg = "red", highlightbackground = "#%02x%02x%02x" % (128, 192, 200)  )
viewData.grid(row = 6,column = 3)

clearData = Button( window, text = "Clear Data", command = lambda: clear_rows(), width = 8, height = 1, fg = "red", highlightbackground = "#%02x%02x%02x" % (128, 192, 200)  )
clearData.grid(row = 6,column = 4)


saveButton = Button( window, text = "Save", command = saveToDB, width = 8, height = 1, fg = "red", highlightbackground = "#%02x%02x%02x" % (128, 192, 200)  )
saveButton.grid(row = 10,column = 5)

exitButton = Button( window, text = "Exit", command = quit_msg, width = 8, height = 1, fg = "red", highlightbackground = "#%02x%02x%02x" % (128, 192, 200)  )
exitButton.grid(row = 10,column = 4)
exitButton.mainloop()

print(view(db,table))

window.mainloop()
