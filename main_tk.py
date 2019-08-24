from tkinter import *
from tkinter import Frame
from tkinter import messagebox
import sqlite3
import csv

from datetime import *
Batch_name = str()
Student_name = str()
topic_name = str()
count = int(1)

class firstPage:
    frame1: Frame

    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="WELCOME", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Choose a option - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.add_button = Button(self.frame1, text='Add a class', width=16, font=("Comic Sans MS", 16), command=self.add)
        self.add_button.pack(pady=20)

        self.update_button = Button(self.frame1, text='Add a student', width=16, font=("Comic Sans MS", 16),
                                    command=self.update)
        self.update_button.pack(pady=20)

        self.att_button = Button(self.frame1, text='Attendance', width=16, font=("Comic Sans MS", 16),
                                  command=self.att_b)
        self.att_button.pack(pady=20)

        self.gen_button = Button(self.frame1, text='Generate CSV', width=16, font=("Comic Sans MS", 16), command=self.csv_button)
        self.gen_button.pack(pady=20)

        self.exit_button = Button(self.frame1, text='Exit', width=16, font=("Comic Sans MS", 16),command=self.exit_b)
        self.exit_button.pack(pady=20)

        self.root.mainloop()

    def att_b(self):
        self.root.destroy()
        attendance()

    def csv_button(self):
        global count
        count = 1
        self.root.destroy()

        csv_b()

    def add(self):

        self.root.destroy()
        add_class()

    def update(self):

        self.root.destroy()
        update_class()

    def exit_b(self):
        self.root.destroy()


class csv_b:
    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="WELCOME", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Enter the batch name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.batch_name = StringVar()

        ##Global

        self.batch_entry = Entry(self.frame1, bd=16, textvar=self.batch_name)
        self.batch_entry.pack(anchor='n')
        global Batch_name
        Batch_name = self.batch_name.get()
        self.add_button = Button(self.frame1, text='Generate', width=16, font=("Comic Sans MS", 16), command=self.csv_bu)
        self.add_button.pack(pady=20)

    def csv_bu(self):

        global count
        conn = sqlite3.connect("main_database.db")
        c = conn.cursor()
        #print('select count(*) from ' + self.batch_name.get())
        c.execute('select count(*) from ' + self.batch_name.get())
        a = c.fetchone()
        if count > a[0]:
            self.root.destroy()
            firstPage()

        # print(a[0])
        c.execute('select * from ' + self.batch_name.get() + ' where Roll_no = ' + str(count))
        student1 = c.fetchone()
        student = student1
        f = open(self.batch_name.get()+".csv", "a+")
        writer = csv.writer(f)
        writer.writerow(student)

        f.close()
        count += 1
        self.csv_bu()
        conn.commit()


class add_class :
    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="ADD", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Enter batch name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.batch_name = StringVar()

        ##Global

        self.batch_entry = Entry(self.frame1, bd=16, textvar=self.batch_name)
        self.batch_entry.pack(anchor='n')

        self.cont_button = Button(self.frame1, text='Continue', width=16, font=("Comic Sans MS", 16),command = self. add_student)

        self.cont_button.pack(pady=20)

    def add_student(self):
        global Batch_name
        Batch_name = self.batch_name.get()
        self.root.destroy()
        add_stu()

class add_stu:
    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="ADD", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Enter Student name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.st_name = StringVar()

        ##Global
        global Student_name
        self.st_entry = Entry(self.frame1, bd=16, textvar=self.st_name)
        self.st_entry.pack(anchor='n')


        self.add_button = Button(self.frame1, text='Add', width=16, font=("Comic Sans MS", 16),command = self.stu)
        self.add_button.pack(pady=20)

        self.done_button = Button(self.frame1, text='Done', width=16, font=("Comic Sans MS", 16),command = self.done)
        self.done_button.pack(pady=20)

    def stu(self):
        if self.st_name:
            conn = sqlite3.connect("main_database.db")
            global Batch_name
            stu_name = str()
            stu_name = self.st_name.get()
            c = conn.cursor()
            c.execute('create table if not exists '+ Batch_name+ ' (Roll_no integer primary key,Name Text)')
            c.execute('insert into ' + Batch_name + '(Name) values("'+stu_name+'")')
            conn.commit()
            self.root.destroy()
            add_stu()

        else:
            messagebox.showinfo("Warning", "Fill enteries")

    def done(self):
        self.root.destroy()
        firstPage()



class update_class :
    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="ADD", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Enter batch name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.batch_name = StringVar()

        ##Global

        self.batch_entry = Entry(self.frame1, bd=16, textvar=self.batch_name)
        self.batch_entry.pack(anchor='n')

        self.cont_button = Button(self.frame1, text='Continue', width=16, font=("Comic Sans MS", 16),command = self. add_student)

        self.cont_button.pack(pady=20)

    def add_student(self):
        global Batch_name
        Batch_name = self.batch_name.get()
        self.root.destroy()
        update_stu()

class update_stu:
    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="ADD", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Enter Student name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.st_name = StringVar()

        ##Global
        global Student_name
        self.st_entry = Entry(self.frame1, bd=16, textvar=self.st_name)
        self.st_entry.pack(anchor='n')


        self.add_button = Button(self.frame1, text='Add', width=16, font=("Comic Sans MS", 16),command = self.stu)
        self.add_button.pack(pady=20)

        self.done_button = Button(self.frame1, text='Done', width=16, font=("Comic Sans MS", 16),command = self.done)
        self.done_button.pack(pady=20)

    def stu(self):
        if self.st_name:
            conn = sqlite3.connect("main_database.db")
            global Batch_name
            stu_name = str()
            stu_name = self.st_name.get()
            c = conn.cursor()
            c.execute('create table if not exists '+ Batch_name+ ' (Roll_no integer primary key,Name Text)')
            c.execute('insert into ' + Batch_name + '(Name) values("'+stu_name+'")')
            conn.commit()
            self.root.destroy()
            firstPage()

        else:
            messagebox.showinfo("Warning", "Fill enteries")

    def done(self):
        self.root.destroy()
        firstPage()

class attendance:
    def __init__(self):
        self.root = Tk()
        self.root.wm_maxsize(1000, 1000)
        self.root.wm_minsize(1000, 1000)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=1000, y=0, width=1000)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="Attendance", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Enter batch name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')

        self.batch_name = StringVar()

        ##Global

        self.batch_entry = Entry(self.frame1, bd=16, textvar=self.batch_name)
        self.batch_entry.pack(anchor='n')
##################

        self.topic_label = Label(self.frame1, text="Enter topic name - ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.topic_label.pack(padx=0, pady=80, anchor='n')

        self.topic_name = StringVar()

        ##Global

        self.topic_entry = Entry(self.frame1, bd=16, textvar=self.topic_name)
        self.topic_entry.pack(anchor='n')

        self.cont_button = Button(self.frame1, text='Continue', width=16, font=("Comic Sans MS", 16),command = self. att_student)

        self.cont_button.pack(pady=20)

    def att_student(self):
        global count
        global Batch_name
        global topic_name
        count = 1
        Batch_name = self.batch_name.get()
        topic_name = self.topic_name.get()  + str("".join((str(date.today()).split('-'))))

        conn = sqlite3.connect("main_database.db")
        c = conn.cursor()
        #print('alter table ' + Batch_name + ' add column ' + topic_name + ' text ')
        c.execute('alter table '+Batch_name+' add column '+topic_name+' text ')

        conn.commit()



        self.root.destroy()
        act()


class act:
    def __init__(self):
        global count



        self.root = Tk()
        self.root.wm_maxsize(800, 800)
        self.root.wm_minsize(800, 800)

        self.frame1 = Frame(self.root, bg='gray')
        self.frame1.place(x=0, height=800, y=0, width=800)
        self.frame1.config()
        self.Welcome_label = Label(self.frame1, text="Attendance", font=('Comic Sans MS', 70), bg='gray', fg='white')
        self.Welcome_label.pack()

        self.Choice_label = Label(self.frame1, text="Choose- ", font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.Choice_label.pack(padx=0, pady=80, anchor='n')



        conn = sqlite3.connect("main_database.db")
        c = conn.cursor()
        # print('alter table ' + Batch_name + ' add column ' + topic_name + ' text ')
        c.execute('select count(*) from '+Batch_name)
        a = c.fetchone()
        if count > a[0]:
            self.root.destroy()
            firstPage()



        #print(a[0])
        c.execute('select Name from ' + Batch_name+' where Roll_no = '+str(count))
        student1 = c.fetchone()
        student = student1[0]
        conn.commit()


        self.st_label = Label(self.frame1, text=student, font=('Comic Sans MS', 45), bg='gray',
                                  fg='white')
        self.st_label.pack(padx=0, pady=80, anchor='n')



        self.present_button = Button(self.frame1, text='Present', width=16, font=("Comic Sans MS", 16),command = self.present)
        self.present_button.pack(pady=20)

        self.absent_button = Button(self.frame1, text='Absent', width=16, font=("Comic Sans MS", 16),command = self.absent)
        self.absent_button.pack(pady=20)


    def present(self):
        global count
        conn = sqlite3.connect("main_database.db")
        c = conn.cursor()
        #print('insert into '+Batch_name+' ('+topic_name+') values("P") where Roll_no = '+str(count))
        c.execute('update '+Batch_name+' set '+topic_name+' = "P" where Roll_no = '+str(count))
        a = c.fetchone()
        # print(a[0])
        conn.commit()

        count += 1
        self.root.destroy()
        act()

    def absent(self):
        global count
        conn = sqlite3.connect("main_database.db")
        c = conn.cursor()
        # print('alter table ' + Batch_name + ' add column ' + topic_name + ' text ')
        c.execute('update '+Batch_name+' set '+topic_name+' = "A" where Roll_no = '+str(count))
        a = c.fetchone()
        # print(a[0])
        conn.commit()

        count += 1
        self.root.destroy()
        act()

f = firstPage()