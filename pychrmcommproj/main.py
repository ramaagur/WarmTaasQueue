import mysql.connector
print("mysql-connector-python is installed and imported successfully.")

# Replace with your actual database credentials
config = {
    'user': 'mysqluser',
    'password': 'Welcome@2024',
    'host': 'localhost',
    'database': 'my_database'

}


try:
    # Establish the connection
    conn = mysql.connector.connect ( **config )
    cursor = conn.cursor ()

    # Define the query
    query = """
    SELECT account.balance_amount 
    FROM account 
    INNER JOIN customer_address ON customer_address.user_add_id = account.id
    INNER JOIN customer_deposits ON customer_deposits.user_id = account.id
    WHERE account.user_name LIKE 'jack%'
    """

    # Execute the query
    cursor.execute(query)

    # Fetch and print results
    for row in cursor.fetchall ():
        print ( row )

    # Close the cursor and connection
    cursor.close ()
    conn.close ()

except mysql.connector.Error as err:
    print ( f"Error: {err}" )
"""
# Establishing the connection
conn = mysql.connector.connect(
    host="root@localhost:3306",    # Replace with your host
    user="root",  # Replace with your MySQL username
    password="Welcome@2024",  # Replace with your MySQL password
    database="my_database"   # Replace with your database name
)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Execute an SQL query using execute() method
cursor.execute("SELECT DATABASE();")

# Fetch the result
db_name = cursor.fetchone()
print("Connected to database:", db_name)

# Closing the connection
conn.close()"""


