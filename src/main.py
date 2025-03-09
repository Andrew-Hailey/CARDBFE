# main.py
from create_database import create_tables, populate_data
import sqlite3
import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk 

open_windows = {}

# Create and populate data
create_tables()
populate_data()


def view_vehicles():
    # check data
    database = sqlite3.connect("Fleet_DB")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()
    for vehicle in vehicles:
        print(vehicle)
    print()
    database.close()
    
def get_vehicle_data():
    # Retrieve data from vehicles table
    database = sqlite3.connect("Fleet_DB")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM vehicles")
    v_data = cursor.fetchall()
    database.close()
    return v_data
    
def on_row_selected(event):
    view_details_button.configure(state="normal")
    

def print_to_log(param):
    print(param)

def open_details_window():
    # Pull data from v_tree
    selected_item = v_tree.focus()
    values = v_tree.item(selected_item, "values")
    vehicle_id = values[0]
    
    # Check if a window is already open for vehicle ID
    if vehicle_id in open_windows:
        open_windows[vehicle_id].lift()
        return
    
    # Create new details window
    sub_details = tk.Toplevel(mainapp)
    sub_details.title("Vehicle Details")
    
    # Add window to dictionary
    open_windows[vehicle_id] = sub_details
    
    # Define variables for widgets
    s_id = tk.StringVar(value=values[0])
    s_type = tk.StringVar(value=values[1])
    s_last_service = tk.StringVar(value=values[2])
    s_next_service = tk.StringVar(value=values[3])
    s_tax_status = tk.StringVar(value=values[4])
    s_age = tk.StringVar(value=values[5])
    s_fuel_type = tk.StringVar(value=values[6])
    
    # Create widgets for window
    id_label = tk.Label(sub_details, text= "ID:")
    id_label.grid(row=0,column=0)
    id_entry = tk.Entry(sub_details, textvariable= s_id)
    id_entry.grid(row=0,column=1)
    id_entry.configure(state="readonly")
    
    type_label = tk.Label(sub_details, text= "Type:")
    type_label.grid(row=1,column=0)
    type_entry = tk.Entry(sub_details, textvariable= s_type)
    type_entry.grid(row=1,column=1)
    
    last_service_label = tk.Label(sub_details, text= "Last Service:")
    last_service_label.grid(row=2,column=0)
    last_service_entry = tk.Entry(sub_details, textvariable= s_last_service)
    last_service_entry.grid(row=2,column=1)    
    
    next_service_label = tk.Label(sub_details, text= "Next Service:")
    next_service_label.grid(row=3,column=0)
    next_service_entry = tk.Entry(sub_details, textvariable= s_next_service)
    next_service_entry.grid(row=3,column=1)
    
    tax_status_label = tk.Label(sub_details, text= "Tax Status:")
    tax_status_label.grid(row=4,column=0)
    tax_status_entry = tk.Entry(sub_details, textvariable= s_tax_status)
    tax_status_entry.grid(row=4,column=1)
    
    age_label = tk.Label(sub_details, text= "Vehicle Age:")
    age_label.grid(row=5,column=0)
    age_entry = tk.Entry(sub_details, textvariable= s_age)
    age_entry.grid(row=5,column=1)
    
    fuel_type_label = tk.Label(sub_details, text= "Fuel Type:")
    fuel_type_label.grid(row=6,column=0)
    fuel_type_entry = tk.Entry(sub_details, textvariable= s_fuel_type)
    fuel_type_entry.grid(row=6,column=1)
    
    # Create buttons
    close_button = tk.Button(sub_details, text="Close", command=lambda: close_window(vehicle_id))
    close_button.grid(row=7,column=1)
    save_button = tk.Button(sub_details, text="Save", command=lambda: print_to_log("saved"))
    save_button.grid(row=7,column=2)
    maintenace_button = tk.Button(sub_details, text="Maintenance Details...", command=lambda: print_to_log("maintenance"))
    maintenace_button.grid(row=7,column=0)

def close_window(vehicle_id):
    #close the current window and remove it from the open_windows dictionary
    if vehicle_id in open_windows:
        open_windows[vehicle_id].destroy()
        del open_windows[vehicle_id]
        
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

# Add button to view vehicle details
view_details_button = tk.Button(mainapp, text="View Vehicle Details...", command=open_details_window, state="disabled")
view_details_button.pack()

# Run the app

mainapp.mainloop()
