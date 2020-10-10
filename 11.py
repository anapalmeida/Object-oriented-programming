import mysql.connector

sql_create = '''CREATE TABLE IF NOT EXISTS teste   ( 
                id_cliente INTEGER NOT NULL AUTO_INCREMENT, 
                nome varCHAR(50) NOT NULL,
                comentario VARCHAR(200),     
                PRIMARY KEY (id_cliente) )'''

try:
    connection = mysql.connector.connect(
        host="uniciddb.mysql.dbaas.com.br",
        user="uniciddb",
        password="Alfa#01",
        database="uniciddb"
    )
    cursor = connection.cursor()
    cursor.execute(sql_create)
    connection.commit()  # efetiva a criação da tabela
    cursor.close()
    connection.close()
    print("Criei a tabela")
except:
    print("Não criei a tabela")
