
from .conexion import ConexionDB
from tkinter import messagebox

# Función que lista la historia médica de un paciente específico
def listarHistoria(idPersona):
    conexion = ConexionDB()
    try:
        # Consulta a la base de datos para obtener la historia médica
        conexion.cursor.execute("""
            SELECT p.apellidoPaterno || ' ' || p.apellidoMaterno AS Apellidos,
                   h.fechaHistoria, h.motivo, h.examenRecibido, h.detalle,
                   h.examenSolicitado, h.tratamiento, h.pendiente, h.idHistoriaMedica
            FROM historiaMedica h
            JOIN Persona p ON h.idPersona = p.idPersona
            WHERE h.idPersona = ?;
        """, (idPersona,))
        
        listaHistoria = conexion.cursor.fetchall()  # Obtener todos los registros
        conexion.cerrarConexion()
        return listaHistoria  # Devolver la lista de historias
    
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al listar la historia médica: {e}")
        return []


def guardarHistoria(idPersona, fechaHistoria, motivo, examenRecibido, detalle, examenSolicitado, tratamiento, pendiente):
    conexion = ConexionDB()
    sql = """INSERT INTO historiaMedica (idPersona, fechaHistoria, motivo, examenRecibido, detalle, examenSolicitado, tratamiento, pendiente) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
  
    try:
        # Ejecutamos la consulta con valores parametrizados
        conexion.cursor.execute(sql, (
            idPersona,  # Cambia de historiaMedica.idPersona a idPersona
            fechaHistoria,
            motivo,
            examenRecibido,
            detalle,
            examenSolicitado,
            tratamiento,
            pendiente,
        ))
        
        # Mostramos un mensaje de éxito
        title = 'Registro Historia Médica'
        mensaje = 'Historia Médica Registrada Exitosamente'
        messagebox.showinfo(title, mensaje)
    
    except Exception as e:
        # Mostramos un mensaje de error con el detalle del problema
        title = 'Registro Historia Médica'
        mensaje = f'ERROR al registrar Historia Médica: {e}'
        messagebox.showerror(title, mensaje)
    
    finally:
        conexion.cerrarConexion()  # Aseguramos que la conexión siempre se cierre


def eliminarHistoria(idHistoriaMedica):
        conexion = ConexionDB()
        sql = f'DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}'

        try:
            conexion.cursor.execute(sql)
            conexion.cerrarConexion()
            title = 'Eliminar Historia Medica'
            mensaje = 'Historia Medica Eliminada Exitosamente'
            messagebox.showinfo(title, mensaje)
        except:
            title: 'Eliminar Historia Medica'
            mensaje = 'ERROR al Intentar Eliminar Historia Medica'
            messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistoria, motivo, examenRecibido, detalle, examenSolicitado, tratamiento, pendiente, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""
    UPDATE historiaMedica 
    SET fechaHistoria = '{fechaHistoria}', 
        motivo = '{motivo}', 
        examenRecibido = '{examenRecibido}', 
        detalle = '{detalle}', 
        examenSolicitado = '{examenSolicitado}', 
        tratamiento = '{tratamiento}', 
        pendiente = '{pendiente}'
    WHERE idHistoriaMedica = {idHistoriaMedica}
    """

    try:
        conexion.cursor.execute(sql)
        #conexion.connection.commit()  # Asegúrate de confirmar los cambios en la base de datos
        title = 'Editar Historia Médica'
        mensaje = 'Historia Médica Editada Exitosamente'
        messagebox.showinfo(title, mensaje)
    
    except Exception as e:
        title = 'Editar Historia Médica'
        mensaje = f'ERROR al Editar Historia Médica: {e}'
        messagebox.showerror(title, mensaje)
    
    finally:
        conexion.cerrarConexion()


class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, examenRecibido, detalle, examenSolicitado, tratamiento, pendiente):

        self.idhistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.examenRecibido = examenRecibido
        self.detalle = detalle
        self.examenSolicitado = examenSolicitado
        self.tratamiento = tratamiento
        self.pendiente = pendiente

    def __str__(self):
        return f'historiaMedica[{self.idPersona}, {self.fechaHistoria}, {self.motivo}, {self.examenRecibido}, {self.detalle}, {self.examenSolicitado}, {self.tratamiento}, {self.pendiente}]'
