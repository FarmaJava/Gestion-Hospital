from connection import obtener_conexion

conexion = obtener_conexion()
cursor = conexion.cursor()

class Paciente:

    def __init__(self):

        self.id_paciente = None
        self.dni = ""
        self.nombre = ""
        self.apellido = ""
        self.fecha_nacimiento = None
        self.telefono = ""
        self.direccion = ""
        self.grupo_sanguineo = ""
        self.antecedentes = ""

    def registrar(self):

        consulta = """
            INSERT INTO Paciente(
                dni,
                nombre,
                apellido,
                fecha_nacimiento,
                telefono,
                direccion,
                grupo_sanguineo,
                antecedentes
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        try:

            cursor.execute(
                consulta,
                (
                    self.dni,
                    self.nombre,
                    self.apellido,
                    self.fecha_nacimiento,
                    self.telefono,
                    self.direccion,
                    self.grupo_sanguineo,
                    self.antecedentes
                )
            )

            conexion.commit()
            return True

        except Exception as e:

            print(e)
            conexion.rollback()
            return False

    def buscar_por_dni(self, dni):

        consulta = """
            SELECT *
            FROM Paciente
            WHERE dni = %s
        """

        cursor.execute(
            consulta,
            (dni,)
        )

        return cursor.fetchone()

    def listar_todos(self):

        cursor.execute(
            "SELECT * FROM Paciente"
        )

        return cursor.fetchall()

    def eliminar(self, id_paciente):

        consulta = """
            DELETE FROM Paciente
            WHERE id_paciente = %s
        """

        cursor.execute(
            consulta,
            (id_paciente,)
        )

        conexion.commit()

    def modificar(self):

        consulta = """
            UPDATE Paciente
            SET
                nombre = %s,
                apellido = %s,
                fecha_nacimiento = %s,
                telefono = %s,
                direccion = %s,
                grupo_sanguineo = %s,
                antecedentes = %s
            WHERE dni = %s
        """

        cursor.execute(
            consulta,
            (
                self.nombre,
                self.apellido,
                self.fecha_nacimiento,
                self.telefono,
                self.direccion,
                self.grupo_sanguineo,
                self.antecedentes,
                self.dni
            )
        )

        conexion.commit()