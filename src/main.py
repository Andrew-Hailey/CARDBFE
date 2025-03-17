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
    """
    Print vehicle data from the database.
    """
    try:
        database = sqlite3.connect("Fleet_DB")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM vehicles")
        vehicles = cursor.fetchall()
        for vehicle in vehicles:
            print(vehicle)
        print()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        if 'database' in locals():
            database.close()


def get_vehicle_data():
    """
    Retrieve vehicle data from the database.
    """
    try:
        database = sqlite3.connect("Fleet_DB")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM vehicles")
        v_data = cursor.fetchall()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        if 'database' in locals():
            database.close()
    return v_data


def on_row_selected(event):
    """
    Enable the 'View Vehicle Details...' button when a row is selected.
    """
    view_details_button.configure(state="normal")


def print_to_log(param):
    """
    Log a message to the console.
    """
    print(param)


def open_details_window():
    """
    Open a details window for a selected vehicle.
    """
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
    s_reg = tk.StringVar(value=values[1])
    s_type = tk.StringVar(value=values[2])
    s_last_service = tk.StringVar(value=values[3])
    s_next_service = tk.StringVar(value=values[4])
    s_tax_status = tk.StringVar(value=values[5])
    s_age = tk.StringVar(value=values[6])
    s_fuel_type = tk.StringVar(value=values[7])

    # Create widgets for window
    labels_and_entries = [
        ("ID:", s_id), 
        ("Registration:", s_reg),
        ("Type:", s_type), 
        ("Last Service:", s_last_service),
        ("Next Service:", s_next_service),
        ("Tax Status:", s_tax_status),
        ("Vehicle Age:", s_age), 
        ("Fuel Type:", s_fuel_type)
    ]
    
    for idx, (label_text, var) in enumerate(labels_and_entries):
        tk.Label(sub_details, text=label_text).grid(row=idx, column=0)
        entry = tk.Entry(sub_details, textvariable=var)
        entry.grid(row=idx, column=1)
        if label_text in ("ID:", "Registration:"):
            entry.configure(state="readonly")

    def close_window(vehicle_id):
        """
        Close the current window and remove it from the open_windows dictionary.
        """
        if vehicle_id in open_windows:
            open_windows[vehicle_id].destroy()
            del open_windows[vehicle_id]

    def open_maintenance_details(vehicle_id):
        """
        Open a maintenance details window for the selected vehicle.
        """
        database = sqlite3.connect("Fleet_DB")
        cursor = database.cursor()
        cursor.execute(
            "SELECT * FROM maintenance_records WHERE vehicle_id = ?", 
            (vehicle_id,)
        )
        maintenance_records = cursor.fetchall()
        database.close()

        # Create maintenance details window
        maintenace_details = tk.Toplevel(mainapp)
        maintenace_details.title(f"Maintenance Details - {vehicle_id}")

        # Create Treeview
        columns = (
            'ID', 'Vehicle ID', 'Maintenance Date', 
            'Description of Work', 'Cost'
        )
        d_tree = ttk.Treeview(
            maintenace_details, columns=columns, show="headings"
        )
        for col in columns:
            d_tree.heading(col, text=col)

        # Insert data
        for record in maintenance_records:
            d_tree.insert("", tk.END, values=record)
        d_tree.pack()

    # Create buttons
    tk.Button(sub_details, text="Close", 
              command=lambda: close_window(vehicle_id)).grid(row=8, column=1)
    tk.Button(sub_details, text="Save", 
              command=lambda: print_to_log("saved")).grid(row=8, column=2)
    tk.Button(sub_details, text="Maintenance Details...", 
              command=lambda: open_maintenance_details(vehicle_id)).grid(row=8, column=0)

    # Handle closing the window
    sub_details.protocol("WM_DELETE_WINDOW", lambda: close_window(vehicle_id))


# Create main application window
mainapp = tk.Tk()
mainapp.title('Fleet Management')
mainapp.geometry("1600x800")
mainapp.rowconfigure(0, weight=1)
mainapp.columnconfigure(1, weight=1)

# Create Treeview
columns = (
    'ID', 'Registration', 'Vehicle Type', 'Last Service Date', 'Next Service Date', 
    'Tax Status', 'Vehicle Age', 'Fuel Type'
)
v_tree = ttk.Treeview(mainapp, columns=columns, show='headings')
for col in columns:
    v_tree.heading(col, text=col)

# Create scrollbars
x_scroll = ttk.Scrollbar(mainapp, orient='horizontal', command=v_tree.xview)
y_scroll = ttk.Scrollbar(mainapp, orient='vertical', command=v_tree.yview)
v_tree.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
x_scroll.grid(row=1, column=1, sticky="ew")
y_scroll.grid(row=0, column=2, sticky="ns")

# Insert data into Treeview
vehicle_data = get_vehicle_data()
for vehicle in vehicle_data:
    v_tree.insert("", tk.END, values=vehicle)

v_tree.grid(row=0, column=1, sticky="nsew")
v_tree.bind("<<TreeviewSelect>>", on_row_selected)

# Add 'View Vehicle Details...' button
view_details_button = tk.Button(
    mainapp, text="View Vehicle Details...", 
    command=open_details_window, state="disabled"
)
view_details_button.grid(row=0, column=0)

# Run the application
mainapp.mainloop()
