
# Replace with your actual database credentials
config = {
    'user': 'root',
    'password': 'Welcome@2024',
    'host': 'localhost',
    'database': 'my_database'
}
try:
    conn =  mysql.connector.connect(user='root',password='Welcome@2024',host='localhost',database='my_database')

    cursor = conn.cursor ()

    # Execute a query
    cursor.execute("SELECT * FROM accounts")

    # Fetch and print results
    for row in cursor.fetchall ():
        print ( row )

    # Close the cursor and connection
    cursor.close ()
    conn.close ()

except mysql.connector.Error as err:
    print ( f"Error: {err}" )
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
