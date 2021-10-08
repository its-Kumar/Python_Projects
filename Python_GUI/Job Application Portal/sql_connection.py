import sqlite3
my_conn = sqlite3.connect('job.db')

import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("1300x250") 

r_set=my_conn.execute('''SELECT * from JOB ''');
i=0 # row value inside the loop 
for JOB in r_set: 
    for j in range(len(JOB)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, JOB[j])
    i=i+1
my_w.mainloop()