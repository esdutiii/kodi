import sqlite3

db_path = r"c:\Users\ortas\OneDrive\Documentos\palantir_fork\plugin.video.eduteamo\moria.cm3"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Search menus table
try:
    cursor.execute("SELECT * FROM menus WHERE label LIKE '%mejor de%' OR sql LIKE '%mejor de%'")
    rows = cursor.fetchall()
    print("Found in menus table:")
    for r in rows:
        print(r)
except Exception as e:
    print("Error querying menus:", e)

conn.close()
