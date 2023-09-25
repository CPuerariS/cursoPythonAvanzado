import psycopg2

conn = psycopg2.connect(
    user="postgres", password="1234", port="5432", host="localhost", database="curso"
)

cursor = conn.cursor()

# Create table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, name VARCHAR(255), age INTEGER, email VARCHAR(255))"
)

# Save data
conn.commit()


# Insert data
cursor.execute(
    "INSERT INTO clientes (name, age, email) VALUES (%s, %s, %s)",
    ("Juan", 25, "juan@mail.com"),
)


cursor.execute(
    "INSERT INTO clientes (name, age, email) VALUES (%s, %s, %s)",
    ("Juan", 30, "juan2@mail.com"),
)

## fetch data and print data
# cursor.execute("SELECT * FROM clientes")
# print(cursor.fetchall())
#
# # fetch one
cursor.execute("SELECT * FROM clientes wHERE name=%s", ("Juan",))
print(cursor.fetchone())
