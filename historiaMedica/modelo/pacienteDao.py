from os import times_result
from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = """UPDATE Persona 
             SET nombre = ?, apellidoPaterno = ?, apellidoMaterno = ?, dni = ?, fechaNacimiento = ?, edad = ?, 
                 nombrePrepagaOS = ?, numeroPrepagaOS = ?, correo = ?, telefono = ?, Alergia = ?, MedicacionActual = ?, 
                 APPClinico = ?, APPQuirurgico = ?, activo = 1 
             WHERE idPersona = ?"""
  
    try:
        # Ejecutamos la consulta con valores parametrizados
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
            idPersona
        ))
                
        # Mostramos un mensaje de éxito
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    
    except Exception as e:
        # Mostramos un mensaje de error con el detalle del problema
        title = 'Editar Paciente'
        mensaje = f'ERROR al Editar Paciente: {e}'
        messagebox.showerror(title, mensaje)
    
    finally:
        conexion.cerrarConexion()  # Aseguramos que la conexión siempre se cierre

# ojooo, ver dni/edad son int por lo cual no llevan comillas simples. el 1 representa activo

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = """INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, dni, fechaNacimiento, edad, nombrePrepagaOS, numeroPrepagaOS, correo, telefono, Alergia, MedicacionActual, APPClinico, APPQuirurgico, activo) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)"""
  
    try:
        # Ejecutamos la consulta con valores parametrizados
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
            persona.APPQuirurgico
        ))
                
        # Mostramos un mensaje de éxito
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    
    except Exception as e:
        # Mostramos un mensaje de error con el detalle del problema
        title = 'Registrar Paciente'
        mensaje = f'ERROR al registrar Paciente: {e}'
        messagebox.showerror(title, mensaje)
    
    finally:
        conexion.cerrarConexion()  # Aseguramos que la conexión siempre se cierre


def listar():
    conexion = ConexionDB()
    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except:
        title = 'Datos'
        mensaje = 'Registro NO EXISTE'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registro NO EXISTE'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Inactivar Registro Paciente'
        mensaje = 'Registro INACTIVADO'
        messagebox.showwarning(title, mensaje)

    except:
        title = 'Inactivar Registro Paciente'
        mensaje = 'ERROR al Inactivar Registro Pte'
        messagebox.showwarning(title, mensaje)




# Definición de la clase Persona
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