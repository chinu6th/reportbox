import psycopg2
from generator import generate_answer


def run_sql_from_generator(query, results):
    """
    Generates SQL using your generator.py and executes it on PostgreSQL.
    Returns the fetched rows.
    """
    # Get SQL from generator
    sql_statement = generate_answer(query, results)

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="tiger",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Execute and fetch
    cur.execute(sql_statement)
    rows = cur.fetchall()

    # Clean up
    cur.close()
    conn.close()

    return rows
