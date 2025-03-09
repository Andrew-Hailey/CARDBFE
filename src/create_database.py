# Import modules
import sqlite3
# Create/Connect to DB
database = sqlite3.connect('Fleet_DB')
# Create a cursor to interact with the DB
cursor = database.cursor()
# Create tables
cursor.execute("CREATE TABLE IF NOT EXISTS vehicles(vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_type TEXT NOT NULL, last_service_date TEXT, next_service_date TEXT, tax_status TEXT, vehicle_age INTEGER, fuel_type TEXT);" )
cursor.execute("CREATE TABLE IF NOT EXISTS maintenance_records(record_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_id INTEGER NOT NULL, maintenance_date TEXT NOT NULL, description_of_work TEXT, cost REAL, FOREIGN KEY(vehicle_id) REFERENCES vehicles(vehicle_id));")
database.commit()
# Check tables
cursor.execute("PRAGMA table_info(vehicles)")
vehicle_table_info = cursor.fetchall()
print("Vehicles table structure:")
for column in vehicle_table_info:
    print(column)

cursor.execute("PRAGMA table_info(maintenance_records)")
maintenance_table_info = cursor.fetchall()
print("Maintenance Records table structure:")
for column in maintenance_table_info:
    print (column)


# Insert base data
cursor.execute("INSERT INTO vehicles (vehicle_type, last_service_date, next_service_date, tax_status, vehicle_age, fuel_type) VALUES ('Car', '2024-03-01', '2025-03-01', 'Paid', 3, 'Petrol'), ('Van', '2023-09-15', '2024-09-15', 'Due', 5, 'Diesel'), ('Truck', '2024-01-20', '2025-01-20', 'Paid', 7, 'Diesel'), ('Pickup Truck', '2022-11-30', '2023-11-30', 'Due', 8, 'Petrol'), ('Car', '2024-06-10', '2025-06-10', 'Paid', 2, 'Electric');")

database.commit()

# Check inserted data

cursor.execute("SELECT * FROM vehicles")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the DB connection
database.close
