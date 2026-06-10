import sqlite3

db_path = r"c:\Users\ortas\OneDrive\Documentos\palantir_fork\plugin.video.eduteamo\moria.cm3"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT item_id, label, icon FROM menus WHERE menu_id = 110")
rows = cursor.fetchall()
print("All items under menu_id = 110:")
for r in rows:
    print(r)

conn.close()
