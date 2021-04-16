'''
Created on Mar 29, 2020

@author: Jordan Yudess
Version 2.2
'''
#Imports
from tkinter import *
from PIL import ImageTk,Image
import pyodbc
import matplotlib.pyplot as plt

#Window creation  
window = Tk()
window.geometry('500x600')
window.title('Data Import Tool')

#Photo Header Image

open_header_image = Image.open("C:/Users/Jordan Yudess/Downloads/DataAnalysis Logo.png")
header_image = ImageTk.PhotoImage(open_header_image)


header_image_label = Label(image = header_image)
header_image_label.place(x = 170, y = 20)

#Text Variables
drivername = StringVar()
servername = StringVar()
database = StringVar()
tablename = StringVar()
 

#Functions
def Close():
    exit()

def PlotGraph():
    for row in cursor:
        plt.plot(row)
    

    
def ShowWindow2():
    window2 = Tk()
    window2.geometry('500x600')
    window2.title('Data Analysis Tool')
    header_label2 = Label(window2, text = "Analysis Tool", width = 15, font = ("arial",14,"bold"))
    #header_label2.place(x = 60, y = 100)
    header_label2.pack()
    
    
    window2_text = Text(window2, height = 8, width = 40)
    window2_text.place(x = 90  , y = 260)
    
    subheader_label2 = Label(window2, text = "Data Returned", width = 30, font = ("arial",12))
    subheader_label2.place(x = 110, y = 220)
    window2_text.config(state = 'normal')
    
    try:
        dn = drivername.get()
        sn = servername.get()
        dd = database.get()
        tn = tablename.get()
        driver_in = 'Driver={%s};' % (dn)
        server_in = 'Server=%s;' % (sn)
        database_in = 'Database = %s;' % (dd)
        trusted_connection_in = 'Trusted_Connection=yes'
        conn = pyodbc.connect(driver_in
                            + server_in
                            + database_in
                            + trusted_connection_in)
        cursor = conn.cursor()
        cursor.execute(('SELECT * FROM %s.dbo.%s') % (dd,tn))
        
        columns = [column[0] for column in cursor.description]
        print(columns)
        window2_text.insert(INSERT, str(columns) + '\n')
        
        
        drivername_label = Label(window2, text = 'Driver Name: %s' % (dn), width = 35, font = ('arial', 12), anchor = W)
        drivername_label.place(x = 85, y = 80)
    
        servername_label = Label(window2, text = 'Server Name: %s' % (sn), width = 35, font = ('arial', 12), anchor = W)
        servername_label.place(x = 85, y = 110)
    
        databasename_label = Label(window2, text = 'Database Name: %s' % (dd), width = 35, font = ('arial', 12), anchor = W)
        databasename_label.place(x = 85, y = 140)
    
        tablename_label = Label(window2, text = 'Table Name: %s' % (tn), width = 35, font = ('arial', 12), anchor = W)
        tablename_label.place(x = 85, y = 170)
        
                
        x2 = []
        y2 = []
        for row in cursor:
            #print(row)
            
            x2.append(int(row[0]))
            y2.append(row[1])
                       
            plt.plot(x2,y2)
            window2_text.insert(INSERT, str(row) + '\n')
        
        
        
        window2_text.config(state = 'disabled')
       
        
        plt.title(('%s v.s %s') % (str(columns[0]),str(columns[1])))
        plt.xlabel(str(columns[0]))
        plt.ylabel(str(columns[1]))
        plt.subplots_adjust(left = 0.20, bottom = 0.20, right = 0.90, top = 0.90, wspace = 0.20, hspace = 0)
        plt.show()
        
    except:
        window2_text.insert(INSERT,"DB info is incorrect. Please try again.")
        window2_text.config(state = 'disabled')
     
 
#Header
header_label = Label(window, text = "Welcome to JY Data Import Tool",relief = "solid", width = 30, font = ("arial",12,"bold"))
header_label.place(x = 100, y = 190)

#DB Details  Header
Connectiondetail_label = Label(window, text = "Connection Details:", width = 15 , font = ("arial",10,"bold"))
Connectiondetail_label.place(x = 130, y = 240)

#DB Details Body
Drivername_label = Label(window, text = "Driver Name: ", width = 15 , font = ("arial",10,'bold'))
Drivername_label.place(x = 114, y = 290)

Drivername_entry = Entry(window, textvar = drivername)
Drivername_entry.place(x = 270, y = 290)

Servername_label = Label(window, text = "Server Name: ", width = 15 , font = ("arial",10,"bold"))
Servername_label.place(x = 115, y = 330)

Servername_entry = Entry(window, textvar = servername) 
Servername_entry.place(x = 270, y = 330)

database_label = Label(window, text = "Database Name: ", width = 20 , font = ("arial",10,"bold"))
database_label.place(x = 103, y = 370)

database_entry = Entry(window, textvar = database)
database_entry.place(x = 270, y = 370)

tablename_label = Label(window, text = "Table Name: ", width = 20 , font = ("arial",10,"bold"))
tablename_label.place(x = 90, y = 410)

tablename_entry = Entry(window, textvar = tablename)
tablename_entry.place(x = 270, y = 410)


#DB Buttons
#connectDB_button = Button(window, text = "Connect DB", bg = 'brown',fg = 'white', width = 10, command = ConnectDB)
#connectDB_button.place(x=150,y=470)


#Close Button
close_button = Button(window, text = "Close", bg = 'brown',fg = 'white', width = 10, command = Close)
close_button.place(x=270,y=470)

dataview_button = Button(window, text = "Connect DB", bg = 'green',fg = 'white', width = 10, command = ShowWindow2)
dataview_button.place(x=170,y=470)

#Main Loop
window.mainloop()




