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
    
def on_row_selected(event):
    selected_item = v_tree.focus()
    values = v_tree.item(selected_item, "values")
    open_details_window(values)


def open_details_window(values):
    sub_details = tk.Toplevel(mainapp)
    sub_details.title("Vehicle Details")
    
    id_label = tk.Label(sub_details, text= "ID:").grid(row=0,column=0)
    id_entry = tk.Entry(sub_details, textvariable= "s_id").grid(row=0,column=1)
    type_label = tk.Label(sub_details, text= "Type:").grid(row=1,column=0)
    type_entry = tk.Entry(sub_details, textvariable= "s_type").grid(row=1,column=1)
    last_service_label = tk.Label(sub_details, text= "Last Service:").grid(row=2,column=0)
    last_service_entry = tk.Entry(sub_details, textvariable= "s_last_service").grid(row=2,column=1)    
    next_service_label = tk.Label(sub_details, text= "Next Service:").grid(row=3,column=0)
    next_service_entry = tk.Entry(sub_details, textvariable= "s_next_service").grid(row=3,column=1)
    tax_status_label = tk.Label(sub_details, text= "Tax Status:").grid(row=4,column=0)
    tax_status_entry = tk.Entry(sub_details, textvariable= "s_tax_status").grid(row=4,column=1)
    age_label = tk.Label(sub_details, text= "Vehicle Age:").grid(row=5,column=0)
    age_entry = tk.Entry(sub_details, textvariable= "s_age").grid(row=5,column=1)
    fuel_type_label = tk.Label(sub_details, text= "Fuel Type:").grid(row=6,column=0)
    fuel_type_entry = tk.Entry(sub_details, textvariable= "s_fuel_type").grid(row=6,column=1)
    
    close_button = tk.Button(sub_details, command=sub_details.destroy).grid(row=7,column=2)
    save_button = tk.Button(sub_details, command=print("saved")).grid(row=7,column=3)
    maintenace_button = tk.Button(sub_details, command=print("maintenance")).grid(row=7,column=1)
    
# Create main window
mainapp = tk.Tk()
mainapp.title('Fleet Management')
mainapp.geometry("1600x800")

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

v_tree.bind("<<TreeviewSelect>>", on_row_selected)

# Add button to view vehicles

button1 = tk.Button(mainapp, text="View Vehicles", command=view_vehicles)
button1.pack()

# Run the app

mainapp.mainloop()
