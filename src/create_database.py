# Import modules
import sqlite3
# Create/Connect to DB
database = sqlite3.connect('Fleet_DB')
# Create a cursor to interact with the DB
cursor = database.cursor()
# Create tables
cursor.execute("CREATE TABLE vehicles(vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_type TEXT NOT NULL, last_service_date TEXT, next_service_date TEXT, tax_status TEXT, vehicle_age INTEGER, fuel_type TEXT);" )
cursor.execute("CREATE TABLE maintenance_records(record_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_id INTEGER NOT NULL FOREIGN KEY(vehicle_id) REFERENCES vehicles(vehicle_id), maintenance_date TEXT NOT NULL, description_of_work TEXT, cost REAL")
database.commit()
# Check tables
cursor.execute("DESCRIBE vehicles")
cursor.execute("DESCRIBE vehicles")


# Insert base data
#cursor.execute("INSERT INTO vehicles ()")
