class Paciente:

    def __init__(
        self,
        dni,
        nombre,
        apellido,
        fecha_nacimiento,
        telefono,
        direccion,
        grupo_sanguineo,
        antecedentes
    ):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.direccion = direccion
        self.grupo_sanguineo = grupo_sanguineo
        self.antecedentes = antecedentes