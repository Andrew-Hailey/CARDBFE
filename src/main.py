# main.py
from create_database import create_tables, populate_data
import sqlite3
import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk 


# Create and populate data
create_tables()
populate_data()
# check data
def view_vehicles():
    database = sqlite3.connect("Fleet_DB")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()
    for vehicle in vehicles:
        print(vehicle)
    print()
    database.close
    
# Retrieve data from vehicles table
def get_vehicle_data():
    database = sqlite3.connect("Fleet_DB")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM vehicles")
    v_data = cursor.fetchall()
    return v_data
    
# Create main window
mainapp = tk.Tk()
mainapp.title('Fleet Management')
mainapp.geometry("400x300")

# Create Treeview
v_tree = ttk.Treeview(mainapp, columns=('ID','Vehicle Type', 'Last Service Date', 'Next Service Date', 'Tax Status', 'Vehicle Age', 'Fuel Type'), show='headings')
v_tree.heading('ID', text='ID')
v_tree.heading('Vehicle Type', text='Vehicle Type')
v_tree.heading('Last Service Date', text='Last Service Date')
v_tree.heading('Next Service Date', text='Next Service Date')
v_tree.heading('Tax Status', text='Tax Status')
v_tree.heading('Vehicle Age', text='Vehicle Age')
v_tree.heading('Fuel Type', text='Fuel Type')

# Add data to the Treeview
vehicle_data = get_vehicle_data()
for vehicle in vehicle_data:
    v_tree.insert("", tk.END, values=vehicle)

v_tree.pack()

# Add button to view vehicles

button1 = tk.Button(mainapp, text="View Vehicles", command=view_vehicles)
button1.pack()

# Run the app

mainapp.mainloop()
