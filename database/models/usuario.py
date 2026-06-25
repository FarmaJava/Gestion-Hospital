from database.connection import obtener_conexion

class Usuario:

 def __init__(self):
        self.id_usuario = None
        self.nombre = ""
        self.usuario = ""
        self.email = ""
        self.contraseña = ""
        self.rol = ""
        
 def login(self, usuario, contraseña):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    consulta = """
        SELECT *
        FROM Usuario
        WHERE email = %s
        AND contraseña = %s
    """

    cursor.execute(
        consulta,
        (usuario, contraseña)
    )

    datos = cursor.fetchone()

    cursor.close()
    conexion.close()

    return datos       
 
 def registrar(self):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    consulta = """
        INSERT INTO Usuario
        (nombre, usuario, email, contraseña, rol)
        VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(
            consulta,
            (
                self.nombre,
                self.usuario,
                self.email,
                self.contraseña,
                self.rol
            )
        )

        conexion.commit()
        return True

    except Exception as e:
        print(e)
        conexion.rollback()
        return False

    finally:
        cursor.close()
        conexion.close()

 def listar_todos(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute(
            "SELECT * FROM Usuario"
        )

        return cursor.fetchall()

 def eliminar(self, id_usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        consulta = """
            DELETE FROM Usuario
            WHERE id_usuario = %s
        """

        cursor.execute(
            consulta,
            (id_usuario,)
        )

        conexion.commit()
        
      
 def existe_usuario(self, usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
      
        consulta = """
            SELECT id_usuario
            FROM Usuario
            WHERE usuario = %s
        """

        cursor.execute(consulta, (usuario,))

        return cursor.fetchone() is not None