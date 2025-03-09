# main.py
from create_database import create_tables, populate_data
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create and populate data
create_tables()
populate_data()

def view_vehicles():
    database = sqlite3.connect("fleet_DB.db")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()
    for vehicle in vehicles:
        print(vehicle)
    database.close
    
# Create main window
mainapp = tk.Tk()
mainapp.title('Fleet Management')

# Add button to view vehicles

button1 = tk.Button(mainapp, text="View Vehicles", command=view_vehicles)
button1.pack()

# Run the app

mainapp.mainloop()
