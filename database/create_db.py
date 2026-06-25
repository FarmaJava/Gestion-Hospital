from connection import obtener_conexion

conexion = obtener_conexion()
cursor = conexion.cursor()

# usuario
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL
)
""")

#paciente
cursor.execute("""
CREATE TABLE IF NOT EXISTS Paciente(
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20),
    direccion VARCHAR(100),
    grupo_sanguineo VARCHAR(10),
    antecedentes TEXT
)
""")

# medico
cursor.execute("""
CREATE TABLE IF NOT EXISTS Medico(
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    matricula VARCHAR(30) UNIQUE NOT NULL,
    especialidad VARCHAR(50),
    telefono VARCHAR(20),
    email VARCHAR(100),

    FOREIGN KEY (id_usuario)
    REFERENCES Usuario(id_usuario)
)
""")

# citas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cita(
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    estado VARCHAR(20),

    FOREIGN KEY (id_paciente)
    REFERENCES Paciente(id_paciente),

    FOREIGN KEY (id_medico)
    REFERENCES Medico(id_medico)
)
""")

# historial medico
cursor.execute("""
CREATE TABLE IF NOT EXISTS Historial_Medico(
    id_historial INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    fecha_registro DATE NOT NULL,
    observaciones TEXT,

    FOREIGN KEY (id_paciente)
    REFERENCES Paciente(id_paciente)
)
""")

#diagnostico
cursor.execute("""
CREATE TABLE IF NOT EXISTS Diagnostico(
    id_diagnostico INT AUTO_INCREMENT PRIMARY KEY,
    id_historial INT NOT NULL,
    id_medico INT NOT NULL,
    fecha DATE NOT NULL,
    sintomas TEXT,
    diagnostico TEXT,

    FOREIGN KEY (id_historial)
    REFERENCES Historial_Medico(id_historial),

    FOREIGN KEY (id_medico)
    REFERENCES Medico(id_medico)
)
""")

# tratamiento
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tratamiento(
    id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    id_diagnostico INT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,

    FOREIGN KEY (id_diagnostico)
    REFERENCES Diagnostico(id_diagnostico)
)
""")

conexion.commit()
conexion.close()