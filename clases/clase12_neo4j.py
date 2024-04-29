from py2neo import Graph


def clase12():
    print("--- CLASE 12: Base Neo4j -----------------------------------------------")
    print("--- 04-04-24 -----------------------------------------------------------")

    # Conexión a la base de datos
    # Para conectarse a la base de datos primero hay que ir a http://http://localhost:7474 y crear una nueva contraseña.
    try:
        graph = Graph("neo4j://localhost:7687", auth=("neo4j", "bigdata-ati"))

        # Crear un nodo
        graph.run("CREATE (a:Person {name: 'Bob'})")
        graph.run("CREATE (a:Person {name: 'Alice'})")
        graph.run("CREATE (a:Person {name: 'Charlie'})")

        # Crear una relación
        graph.run(
            "MATCH (a:Person), (b:Person) WHERE a.name = 'Bob' AND b.name = 'Alice' CREATE (a)-[r:KNOWS]->(b) RETURN r")
        graph.run(
            "MATCH (a:Person), (b:Person) WHERE a.name = 'Alice' AND b.name = 'Charlie' CREATE (a)-[r:KNOWS]->(b) RETURN r")

        # Consultar nodos
        print("--- Nodos ----------------")
        nodes = graph.run("MATCH (n) RETURN n")
        for node in nodes:
            print(node)

        # Consultar relaciones
        print("--- Relaciones ------------")
        relationships = graph.run("MATCH ()-[r]->() RETURN r")
        for relationship in relationships:
            print(relationship)

        # Consultar nodos y relaciones
        print("--- Nodos y relaciones -----")
        nodes_and_relationships = graph.run("MATCH (n)-[r]->(m) RETURN n, r, m")
        for node_and_relationship in nodes_and_relationships:
            print(node_and_relationship)

        # Eliminar el grafo
        graph.run("MATCH (n) DETACH DELETE n")

    except Exception as e:
        print("Error de conexión: ", e)
        print("No se puede ejecutar clase 12 - Iniciar docker con Neo4j")
