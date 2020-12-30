import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="daniel", 
                                  database="Api")
cursor1=conexion1.cursor()

rows_count = cursor.execute(query_sql)
if rows_count < 1:

    sql="insert into Usuarios(acceso, nombre, clave) values (%s,%s,%s)"
    datos=("super", "admins sys", "123tec")
    cursor1.execute(sql, datos)
    conexion1.commit()
    conexion1.close()
    print("Usuario super creado")

else:
    print("Ya existe usuario super")
