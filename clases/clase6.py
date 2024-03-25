import psycopg2

def clase6():
    print("--- CLASE 6: base relacional -------------------------------------------")

    class PostgreSQLConnection:
        def __init__(self, dbname, user, password, host='localhost', port=5432):
            self.dbname = dbname
            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.connection = None
            self.cursor = None

        def connect(self):
            try:
                self.connection = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port
                )
                self.cursor = self.connection.cursor()
                print("Connected to PostgreSQL database!")
            except psycopg2.Error as e:
                print("Unable to connect to the PostgreSQL database:", e)
                raise e  # re-raise the exception to stop the program

        def execute_query(self, query):
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print("Query executed successfully!")
            except psycopg2.Error as e:
                print("Error executing query:", e)

        def fetch_data(self, query):
            try:
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except psycopg2.Error as e:
                print("Error fetching data:", e)

        def close(self):
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("Connection closed.")

    # Example usage:
    # Initialize PostgreSQL connection
    postgres_conn = PostgreSQLConnection(dbname='bigd-db', user='postgres', password='bigData1234')

    # Connect to the database
    postgres_conn.connect()

    # Execute a query for create a table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        hire_date DATE NOT NULL
    );
    '''
    postgres_conn.execute_query(create_table_query)

    # Insert some data
    insert_query = '''
    INSERT INTO employees (first_name, last_name, email, hire_date)
    VALUES
        ('John', 'Doe', 'johndoe@example.com', '2022-01-01');
    INSERT INTO employees (first_name, last_name, email, hire_date)
    VALUES
        ('Jane', 'Doe', 'janedoe@example.com', '2022-01-02');
    '''
    # postgres_conn.execute_query(insert_query)  # Uncomment this line to insert data

    # Fetch data
    select_query = 'SELECT * FROM employees;'

    rows = postgres_conn.fetch_data(select_query)

    for row in rows:
        print(row)

    # Close the connection
    postgres_conn.close()

