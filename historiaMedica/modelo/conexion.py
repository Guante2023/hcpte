import sqlite3
from tkinter import messagebox

# Clase para manejar la conexión a la base de datos
class ConexionDB:
    def __init__(self, baseDatos='database/dbhistorial.db'):
        self.baseDatos = baseDatos
        try:
            self.conexion = sqlite3.connect(self.baseDatos)
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a la base de datos:", self.baseDatos)
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos {self.baseDatos}: {e}")
            self.conexion = None

    def cerrarConexion(self):
        if self.conexion:
            try:
                self.conexion.commit()
                self.conexion.close()
                print("Conexión cerrada correctamente.")
            except sqlite3.Error as e:
                print(f"Error al cerrar la conexión: {e}")

# Verifica si la tabla Persona existe
def verificar_tabla(conexion):
    try:
        conexion.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Persona';")
        result = conexion.cursor.fetchone()
        if result:
            print("La tabla 'Persona' existe.")
        else:
            print("La tabla 'Persona' no existe.")
    except sqlite3.Error as e:
        print(f"Error al verificar la tabla 'Persona': {e}")

# Crea la tabla Persona si no existe
def crear_tabla_persona(conexion):
    try:
        conexion.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Persona (
                idPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellidoPaterno TEXT NOT NULL,
                apellidoMaterno TEXT NOT NULL,
                dni INTEGER NOT NULL,
                fechaNacimiento TEXT NOT NULL,
                edad INTEGER NOT NULL,
                nombrePrepagaOS TEXT,
                numeroPrepagaOS TEXT,
                correo TEXT,
                telefono TEXT,
                Alergia TEXT,
                MedicacionActual TEXT,
                APPClinico TEXT,
                APPQuirurgico TEXT,
                activo INTEGER NOT NULL
            );
        """)
        print("Tabla 'Persona' creada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla 'Persona': {e}")

# Función para insertar un nuevo paciente en la tabla Persona
def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = """INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, dni, fechaNacimiento, edad, nombrePrepagaOS, numeroPrepagaOS, correo, telefono, Alergia, MedicacionActual, APPClinico, APPQuirurgico, activo) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
  
    try:
        # Ejecutar la consulta SQL con los valores parametrizados
        conexion.cursor.execute(sql, (
            persona.nombre,
            persona.apellidoPaterno,
            persona.apellidoMaterno,
            persona.dni,
            persona.fechaNacimiento,
            persona.edad,
            persona.nombrePrepagaOS,
            persona.numeroPrepagaOS,
            persona.correo,
            persona.telefono,
            persona.Alergia,
            persona.MedicacionActual,
            persona.APPClinico,
            persona.APPQuirurgico,
            1  # activo
        ))
        conexion.cerrarConexion()
        
        # Mostrar mensaje de éxito
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    
    except Exception as e:
        # Mostrar mensaje de error con el detalle del problema
        title = 'Registrar Paciente'
        mensaje = f'ERROR al registrar Paciente: {str(e)}'
        messagebox.showerror(title, mensaje)

# Clase que representa a una persona (paciente)
class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, dni, fechaNacimiento, edad, nombrePrepagaOS, numeroPrepagaOS, correo, telefono, Alergia, MedicacionActual, APPClinico, APPQuirurgico):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.nombrePrepagaOS = nombrePrepagaOS
        self.numeroPrepagaOS = numeroPrepagaOS
        self.correo = correo
        self.telefono = telefono
        self.Alergia = Alergia
        self.MedicacionActual = MedicacionActual
        self.APPClinico = APPClinico
        self.APPQuirurgico = APPQuirurgico
    
    def __str__(self):
        return f'Persona[{self.nombre}, {self.apellidoPaterno}, {self.apellidoMaterno}, {self.dni}, {self.fechaNacimiento}, {self.edad}, {self.nombrePrepagaOS}, {self.numeroPrepagaOS}, {self.correo}, {self.telefono}, {self.Alergia}, {self.MedicacionActual}, {self.APPClinico}, {self.APPQuirurgico}]'

# Iniciar la base de datos: verificar y crear la tabla si es necesario
def iniciar_db():
    conexion = ConexionDB()
    
    # Verificar si la tabla 'Persona' existe
    verificar_tabla(conexion)
    
    # Si no existe, crear la tabla
    crear_tabla_persona(conexion)
    
    conexion.cerrarConexion()

# Ejecutar la inicialización de la base de datos
iniciar_db()
