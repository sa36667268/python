import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
mycursor.execute("USE test")
mycursor.execute("select * from emp")
column_names = [desc[0] for desc in mycursor.description]
rows = mycursor.fetchall()

# Calculate column widths
col_widths = [max(len(str(col)), max(len(str(row[i])) for row in rows)) for i, col in enumerate(column_names)]

# Print column headers
header = "  ".join(str(col).ljust(col_widths[i]) for i, col in enumerate(column_names))
print(header)
print("-" * len(header))

# Print rows
for row in rows:
  print("  ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)))
