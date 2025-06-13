# Lesson 15 homework

# Step 1: Creating the Database and Table

import sqlite3

# Connecting to database (creates new one if it doesn't exist)

conn = sqlite3.connect("starfleet.db")
cursor = conn.cursor()

# Creating table 

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Step 2: Populating the Table with Given Data

# Inserting data

cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

conn.commit()

# Step 3: Update Name of "Jadzia Dax" to "Ezri Dax"

cursor.execute('''
UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'
''')

conn.commit()

# Step 4: Display Name and Age of All Bajorans

cursor.execute('''
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
''')

results = cursor.fetchall()

print("Bajoran crew members:")
for name, age in results:
    print(f" - {name}, Age: {age}")

# Final Cleanup

conn.close() 
