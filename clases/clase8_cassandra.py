from cassandra.cluster import Cluster


def clase8():
    print("--- CLASE 8: Base Cassandra --------------------------------------------")
    print("--- 20-03-24 -----------------------------------------------------------")
    # Connect to the local Cassandra instance
    cluster = Cluster(['localhost'], port=9042)
    try:
        session = cluster.connect()
        print("Connected to the cluster in Cassandra")
    except Exception as e:
        print("Error:", e)
        print("Make sure that Cassandra is running on localhost and port 9042")
        print("No se puede ejecutar clase 8 - Iniciar docker con Cassandra")
        return

    # Create a keyspace (if needed)
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};")

    # Use the keyspace
    session.set_keyspace('my_keyspace')

    # Drop the table (if needed)
    session.execute("DROP TABLE IF EXISTS my_table;")

    # Create a table (if needed)
    session.execute("CREATE TABLE IF NOT EXISTS my_table (id UUID PRIMARY KEY, name TEXT);")

    # Insert data into the table
    session.execute("INSERT INTO my_table (id, name) VALUES (uuid(), 'Nicolas Fernandez');")

    # Query data from the table
    rows = session.execute("SELECT * FROM my_table;")

    print("Data in the table: ------------")
    for row in rows:
        print(row.id, row.name)
    print("--------------------------------")
    # Close the session and cluster connection
    session.shutdown()
    cluster.shutdown()
    print("Disconnected from the cluster in Cassandra")
