import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="tiger",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Query data
cur.execute("SELECT * FROM dim_customer;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
