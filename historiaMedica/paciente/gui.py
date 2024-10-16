import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date



class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg="#CDD8FF")
        self.idPersona = None #Para no tener conflictos,  ver deshabilitar
        self.camposPaciente()        
        self.deshabilitar()
        self.tablaPaciente()

        
    def camposPaciente(self):

        ###  LABELS  ###
        self.lblnombre = tk.Label(self, text="Nombre: ")
        self.lblnombre.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblnombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApPaterno = tk.Label(self, text="Apellido Paterno: ")
        self.lblApPaterno.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblApPaterno.grid(column=0, row=1, padx=10, pady=5)

        self.lblApMaterno = tk.Label(self, text="Apellido Materno: ")
        self.lblApMaterno.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblApMaterno.grid(column=0, row=2, padx=10, pady=5)

        self.lblDNI = tk.Label(self, text="DNI: ")
        self.lblDNI.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblDNI.grid(column=0, row=3, padx=10, pady=5)

        self.lblFNacimiento = tk.Label(self, text="Fecha Nacimiento: ")
        self.lblFNacimiento.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblFNacimiento.grid(column=0, row=4, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text="Edad: ")
        self.lblEdad.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblEdad.grid(column=0, row=5, padx=10, pady=5)

        
        self.lblprepagaOs = tk.Label(self, text="Prepaga/OS: ")
        self.lblprepagaOs.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblprepagaOs.grid(column=0, row=6, padx=10, pady=5)

        self.lblNprepagaOs = tk.Label(self, text="Numero prepaga/OS: ")
        self.lblNprepagaOs.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblNprepagaOs.grid(column=0, row=7, padx=10, pady=5)

        self.lblcorreo = tk.Label(self, text="Correo: ")
        self.lblcorreo.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblcorreo.grid(column=0, row=8, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text="Telefono: ")
        self.lblTelefono.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblTelefono.grid(column=0, row=9, padx=10, pady=5)

        self.lblAlergia = tk.Label(self, text="Alergia: ")
        self.lblAlergia.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblAlergia.grid(column=0, row=10, padx=10, pady=5)

        self.lblMedActual = tk.Label(self, text="Medicación Actual: ")
        self.lblMedActual.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblMedActual.grid(column=0, row=11, padx=10, pady=5)

        self.lblAppCli = tk.Label(self, text="APPClinico: ")
        self.lblAppCli.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblAppCli.grid(column=0, row=12, padx=10, pady=5)

        self.lblAppQx = tk.Label(self, text="APPquirurgico: ")
        self.lblAppQx.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblAppQx.grid(column=0, row=13, padx=10, pady=5)

        

        ###  ENTRYS  ###
        self.svnombre = tk.StringVar()
        self.entrynombre = tk.Entry(self, textvariable=self.svnombre)
        self.entrynombre.config(width=50, font=("ARIAL", 15))
        self.entrynombre.grid(column=1, row=0, padx=10, pady=5, columnspan = 2)

        self.svApPaterno= tk.StringVar()
        self.entryApPaterno = tk.Entry(self, textvariable=self.svApPaterno)
        self.entryApPaterno.config(width=50, font=("ARIAL", 15))
        self.entryApPaterno.grid(column=1, row=1, padx=10, pady=5, columnspan = 2)

        self.svApMaterno = tk.StringVar()
        self.entryApMaterno = tk.Entry(self, textvariable=self.svApMaterno)
        self.entryApMaterno.config(width=50, font=("ARIAL", 15))
        self.entryApMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan = 2)

        
        self.svDNI = tk.StringVar()
        self.entryDNI = tk.Entry(self, textvariable=self.svDNI)
        self.entryDNI.config(width=50, font=("ARIAL", 15))
        self.entryDNI.grid(column=1, row=3, padx=10, pady=5, columnspan = 2)

        self.svFNacimiento= tk.StringVar()
        self.entryFNacimiento = tk.Entry(self, textvariable=self.svFNacimiento)
        self.entryFNacimiento.config(width=50, font=("ARIAL", 15))
        self.entryFNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan = 2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=("ARIAL", 15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5, columnspan = 2)

        
        self.svprepagaOS = tk.StringVar()
        self.entryprepagaOS = tk.Entry(self, textvariable=self.svprepagaOS)
        self.entryprepagaOS.config(width=50, font=("ARIAL", 15))
        self.entryprepagaOS.grid(column=1, row=6, padx=10, pady=5, columnspan = 2)

        self.svNprepagaOs= tk.StringVar()
        self.entryNprepagaOS = tk.Entry(self, textvariable=self.svNprepagaOs)
        self.entryNprepagaOS.config(width=50, font=("ARIAL", 15))
        self.entryNprepagaOS.grid(column=1, row=7, padx=10, pady=5, columnspan = 2)

        self.svcorreo = tk.StringVar()
        self.entrycorreo = tk.Entry(self, textvariable=self.svcorreo)
        self.entrycorreo.config(width=50, font=("ARIAL", 15))
        self.entrycorreo.grid(column=1, row=8, padx=10, pady=5, columnspan = 2)

        
        self.svtelefono = tk.StringVar()
        self.entrytelefono = tk.Entry(self, textvariable=self.svtelefono)
        self.entrytelefono.config(width=50, font=("ARIAL", 15))
        self.entrytelefono.grid(column=1, row=9, padx=10, pady=5, columnspan = 2)

        self.svAlergia= tk.StringVar()
        self.entryAlergia = tk.Entry(self, textvariable=self.svAlergia)
        self.entryAlergia.config(width=50, font=("ARIAL", 15))
        self.entryAlergia.grid(column=1, row=10, padx=10, pady=5, columnspan = 2)

        self.svMedActual = tk.StringVar()
        self.entryMedActual = tk.Entry(self, textvariable=self.svMedActual)
        self.entryMedActual.config(width=50, font=("ARIAL", 15))
        self.entryMedActual.grid(column=1, row=11, padx=10, pady=5, columnspan = 2)

        
        self.svAPPCli = tk.StringVar()
        self.entryAPPCli = tk.Entry(self, textvariable=self.svAPPCli)
        self.entryAPPCli.config(width=50, font=("ARIAL", 15))
        self.entryAPPCli.grid(column=1, row=12, padx=10, pady=5, columnspan = 2)

        self.svAPPQx= tk.StringVar()
        self.entryAPPQx = tk.Entry(self, textvariable=self.svAPPQx)
        self.entryAPPQx.config(width=50, font=("ARIAL", 15))
        self.entryAPPQx.grid(column=1, row=13, padx=10, pady=5, columnspan = 2)

        

        #################### BUTTONS BUTTONS BUTTONS #######################

        self.btnNuevo = tk.Button(self, text = "Nuevo", command=self.habilitar )        
        self.btnNuevo.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.btnNuevo.grid(column=0, row=15, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text = "Guardar", command =self.guardarPaciente)        
        self.btnGuardar.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.btnGuardar.grid(column=1, row=15, padx=10, pady=5)


        self.btnCancelar = tk.Button(self, text = "Cancelar", command=self.deshabilitar)        
        self.btnCancelar.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#B00000", cursor="hand2", activebackground="#D27C7C")
        self.btnCancelar.grid(column=2, row=15, padx=10, pady=5)


        ####################       BUSCADOR             #################
        #LABEL Buscador
        self.lblBuscardni = tk.Label(self, text = 'Buscar DNI: ')
        self.lblBuscardni.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblBuscardni.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarapellido = tk.Label(self, text = 'Buscar Apellido: ')
        self.lblBuscarapellido.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblBuscarapellido.grid(column=3, row=1, padx=10, pady=5)

        self.lblBuscarId = tk.Label(self, text = 'Buscar ID: ')
        self.lblBuscarId.config(font=("ARIAL", 15, "bold"), bg="#CDD8FF")
        self.lblBuscarId.grid(column=3, row=2, padx=10, pady=5)

        #ENTRY Buscador
        self.svBuscarDNI = tk.StringVar()
        self.entryBuscarDNI = tk.Entry(self, textvariable=self.svBuscarDNI)
        self.entryBuscarDNI.config(width=20, font=("ARIAL", 15))
        self.entryBuscarDNI.grid(column=4, row=0, padx=10, pady=5, columnspan = 2)

        self.svBuscarapellido = tk.StringVar()
        self.entryBuscarapellido = tk.Entry(self, textvariable=self.svBuscarapellido)
        self.entryBuscarapellido.config(width=20, font=("ARIAL", 15))
        self.entryBuscarapellido.grid(column=4, row=1, padx=10, pady=5, columnspan = 2)

        self.svBuscarId = tk.StringVar()
        self.entryBuscarId = tk.Entry(self, textvariable=self.svBuscarId)
        self.entryBuscarId.config(width=20, font=("ARIAL", 15))
        self.entryBuscarId.grid(column=4, row=2, padx=10, pady=5, columnspan = 2)

        #BUTTON Buscador

        self.btnBuscarCondicion = tk.Button(self, text = "Buscar", command=self.buscarCondicion)        
        self.btnBuscarCondicion.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#00396F", cursor="hand2", activebackground="#588D8D")
        self.btnBuscarCondicion.grid(column=3, row=3, padx=10, pady=5, columnspan = 1)

        self.btnlimpiarBuscador = tk.Button(self, text = "Ir a Lista Actual", command=self.limpiarBuscador)        
        self.btnlimpiarBuscador.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#00396F", cursor="hand2", activebackground="#588D8D")
        self.btnlimpiarBuscador.grid(column=4, row=3, padx=10, pady=5, columnspan = 1)



        

        ####################       CALENDARIO           #################
        # Variables asociadas a campos
        self.svFNacimiento = StringVar()  # Para almacenar la fecha de nacimiento
        self.svEdad = StringVar()         # Para almacenar la edad calculada

        
        self.btnCalendario = tk.Button(self, text="Calendario", command=self.vistaCalendario)
        self.btnCalendario.config(width=12, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#76936E", cursor="hand2", activebackground="#588D8D")
        self.btnCalendario.grid(column=3, row=4, padx=10, pady=5, columnspan=1)

        # Campo de entrada (Entry) para la fecha de nacimiento, asociado a svFNacimiento
        self.entryFNacimiento = tk.Entry(self, textvariable=self.svFNacimiento, font=("ARIAL", 12))
        self.entryFNacimiento.grid(column=1, row=4, padx=10, pady=5)

        # Entry para la edad, asociado a svEdad (no es necesario un nuevo Label)
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad, font=("ARIAL", 12))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(0, 0)

        # Configuración del calendario
        self.calendar = Calendar(
            self.calendario,
            selectmode='day',
            year=1990,
            month=1,
            day=1,
            locale='es_US',  # Asegúrate de que este locale sea correcto
            date_pattern='dd-mm-Y'
        )
        self.calendar.grid(row=1, column=0)

        # Botón para confirmar la selección de fecha
        btnConfirmar = tk.Button(self.calendario, text="Confirmar", command=self.enviarFecha)
        btnConfirmar.grid(row=2, column=0, pady=10)

    def enviarFecha(self):
        # Obtener la fecha seleccionada del calendario
        fecha_seleccionada = self.calendar.get_date()

        # Establecer la fecha seleccionada en el StringVar asociado al Entry de fecha de nacimiento
        self.svFNacimiento.set(fecha_seleccionada)

        # Cerrar la ventana del calendario
        self.calendario.destroy()

        # Llamar a la función calcularEdad automáticamente
        self.calcularEdad()

    def calcularEdad(self):
        try:
            # Obtener la fecha actual
            fecha_actual = date.today()

            # Obtener la fecha de nacimiento del StringVar (svFNacimiento)
            fecha_nacimiento_str = self.svFNacimiento.get()

            # Verificar que se haya seleccionado una fecha
            if fecha_nacimiento_str == "":
                self.svEdad.set("Selecciona fecha")
                return

            # Convertir la fecha de nacimiento de String a objeto datetime
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d-%m-%Y").date()

            # Calcular la edad
            edad = fecha_actual.year - fecha_nacimiento.year
            if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1

            # Enviar la edad calculada al StringVar svEdad
            self.svEdad.set(str(edad))

        except ValueError:
            # Manejo de error en caso de que el formato de la fecha no sea válido
            self.svEdad.set("Error en fecha")






        
    def limpiarBuscador(self):
        self.svBuscarDNI.set('')
        self.svBuscarapellido.set('')
        self.svBuscarId.set('')
        self.tablaPaciente()


    def buscarCondicion(self):
        if len(self.svBuscarDNI.get()) > 0 or len(self.svBuscarapellido.get()) > 0 or len(self.svBuscarId.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDNI.get())) > 0:
                where = "WHERE dni = " + self.svBuscarDNI.get() + "" #WHERE dni = no se usa comilla simple xq es int
            if (len(self.svBuscarId.get())) > 0:
                where = "WHERE idPersona = " + self.svBuscarId.get() + "" #WHERE Id = no se usa comilla simple xq es int

            if (len(self.svBuscarapellido.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svBuscarapellido.get() + "%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()




    
    def guardarPaciente(self):
        persona = Persona(self.svnombre.get(), self.svApPaterno.get(), self.svApMaterno.get(), self.svDNI.get(),
        self.svFNacimiento.get(),self.svEdad.get(), self.svprepagaOS.get(), self.svNprepagaOs.get(), 
        self.svcorreo.get(), self.svtelefono.get(), self.svAlergia.get(), self.svMedActual.get(), 
        self.svAPPCli.get(), self.svAPPQx.get()
        )
        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona,self.idPersona)
        
        
        self.deshabilitar()#borra el campo cargadoy lo deshabilita
        self.tablaPaciente()#refresca tabla al guardar

    def habilitar(self):
        
        self.svnombre.set('')
        self.svApPaterno.set('')
        self.svApMaterno.set('')
        self.svDNI.set('')
        self.svFNacimiento.set('')
        self.svEdad.set('')
        self.svprepagaOS.set('')
        self.svNprepagaOs.set('')
        self.svcorreo.set('')
        self.svtelefono.set('')
        self.svAlergia.set('')
        self.svMedActual.set('')
        self.svAPPCli.set('')
        self.svAPPQx.set('')


        self.entrynombre.config(state='normal')        
        self.entryApPaterno.config(state='normal')        
        self.entryApMaterno.config(state='normal')        
        self.entryDNI.config(state='normal')        
        self.entryFNacimiento.config(state='normal')        
        self.entryEdad.config(state='normal')        
        self.entryprepagaOS.config(state='normal')        
        self.entryNprepagaOS.config(state='normal')        
        self.entrycorreo.config(state='normal')      
        self.entrytelefono.config(state='normal')       
        self.entryAlergia.config(state='normal')        
        self.entryMedActual.config(state='normal')        
        self.entryAPPCli.config(state='normal')        
        self.entryAPPQx.config(state='normal')
        
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')


    def deshabilitar(self):
        self.idPersona = None
        self.svnombre.set('')
        self.svApPaterno.set('')
        self.svApMaterno.set('')
        self.svDNI.set('')
        self.svFNacimiento.set('')
        self.svEdad.set('')
        self.svprepagaOS.set('')
        self.svNprepagaOs.set('')
        self.svcorreo.set('')
        self.svtelefono.set('')
        self.svAlergia.set('')
        self.svMedActual.set('')
        self.svAPPCli.set('')
        self.svAPPQx.set('')


        
        self.entrynombre.config(state='disabled')        
        self.entryApPaterno.config(state='disabled')        
        self.entryApMaterno.config(state='disabled')        
        self.entryDNI.config(state='disabled')        
        self.entryFNacimiento.config(state='disabled')        
        self.entryEdad.config(state='disabled')        
        self.entryprepagaOS.config(state='disabled')        
        self.entryNprepagaOS.config(state='disabled')        
        self.entrycorreo.config(state='disabled')      
        self.entrytelefono.config(state='disabled')       
        self.entryAlergia.config(state='disabled')        
        self.entryMedActual.config(state='disabled')        
        self.entryAPPCli.config(state='disabled')        
        self.entryAPPQx.config(state='disabled')
        
        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')

    def tablaPaciente(self, where=""):
        
        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse() (ojoo revierte orden de aparición en tabla)

        self.tabla = ttk.Treeview(self, column = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'dni', 'fechaNacimiento', 'edad', 'nombrePrepagaOS', 'numeroPrepagaOS', 'correo', 'telefono', 'Alergia', 'MedicacionActual', 'APPClinico', 'APPQuirurgico'), height=5)
        self.tabla.grid(column = 0, row = 16, columnspan = 15, sticky = 'nse')

        self.scroll = ttk.Scrollbar(self, orient = 'vertical', command = self.tabla.yview)
        self.scroll.grid(row=16, column=17, sticky = 'nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)
        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0', text='Id')
        self.tabla.heading('#1', text='nombre')
        self.tabla.heading('#2', text='apellidoPaterno')
        self.tabla.heading('#3', text='apellidoMaterno')
        self.tabla.heading('#4', text='dni')
        self.tabla.heading('#5', text='fechaNacimiento')
        self.tabla.heading('#6', text='edad')
        self.tabla.heading('#7', text='nombrePrepagaOS')
        self.tabla.heading('#8', text='numeroPrepagaOS')
        self.tabla.heading('#9', text='correo')
        self.tabla.heading('#10', text='telefono')
        self.tabla.heading('#11', text='Alergia')
        self.tabla.heading('#12', text='MedicacionActual')
        self.tabla.heading('#13', text='APPClinico')
        self.tabla.heading('#14', text='APPQx')

        self.tabla.column('#0', anchor=W, width=50)
        self.tabla.column('#1', anchor=W, width=150)
        self.tabla.column('#2', anchor=W, width=150)
        self.tabla.column('#3', anchor=W, width=150)
        self.tabla.column('#4', anchor=W, width=50)
        self.tabla.column('#5', anchor=W, width=50)
        self.tabla.column('#6', anchor=W, width=50)
        self.tabla.column('#7', anchor=W, width=50)
        self.tabla.column('#8', anchor=W, width=50)
        self.tabla.column('#9', anchor=W, width=50)
        self.tabla.column('#10', anchor=W, width=50)
        self.tabla.column('#11', anchor=W, width=150)
        self.tabla.column('#12', anchor=W, width=150)
        self.tabla.column('#13', anchor=W, width=50)
        self.tabla.column('#14', anchor=W, width=50)
        
        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13],p[14]), tags=('evenrow',))
        
        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command= self.editarPaciente)
        self.btnEditarPaciente.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#1E0075", cursor="hand2", activebackground="#35BD6F")
        self.btnEditarPaciente.grid(column=0, row=21, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command = self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#8A0000", cursor="hand2", activebackground="#D58A8A")
        self.btnEliminarPaciente.grid(column=1, row=21, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente')
        self.btnHistorialPaciente.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#007C79", cursor="hand2", activebackground="#99F2F0")
        self.btnHistorialPaciente.grid(column=2, row=21, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Salir', command = self.root.destroy)
        self.btnHistorialPaciente.config(width=20, font=("ARIAL", 12, "bold"), fg="#DAD5D6", bg="#30B10C", cursor="hand2", activebackground="#35BD6F")
        self.btnHistorialPaciente.grid(column=4, row=21, padx=10, pady=5)



    def editarPaciente(self):
        try:
            # Obtener el ID del paciente seleccionado
            self.idPersona = self.tabla.item(self.tabla.selection())['text']  # trae el Id
            
            # Obtener los valores seleccionados (nombre, apellidos, etc.)
            self.nombre = self.tabla.item(self.tabla.selection())['values'][0]  # trae el nombre
            self.ApPaterno = self.tabla.item(self.tabla.selection())['values'][1]
            self.ApMaterno = self.tabla.item(self.tabla.selection())['values'][2]
            self.DNI = self.tabla.item(self.tabla.selection())['values'][3]
            self.FNacimiento = self.tabla.item(self.tabla.selection())['values'][4]
            self.Edad = self.tabla.item(self.tabla.selection())['values'][5]
            self.prepagaOS = self.tabla.item(self.tabla.selection())['values'][6]
            self.NprepagaOS = self.tabla.item(self.tabla.selection())['values'][7]
            self.correo = self.tabla.item(self.tabla.selection())['values'][8]
            self.telefono = self.tabla.item(self.tabla.selection())['values'][9]
            self.Alergia = self.tabla.item(self.tabla.selection())['values'][10]
            self.MedActual = self.tabla.item(self.tabla.selection())['values'][11]
            self.APPCli = self.tabla.item(self.tabla.selection())['values'][12]
            self.APPQx = self.tabla.item(self.tabla.selection())['values'][13]

            # Habilitar la edición de campos
            self.habilitar()

            # Insertar los valores en los campos de entrada correspondientes
            self.entrynombre.insert(0, self.nombre)
            self.entryApPaterno.insert(0, self.ApPaterno)
            self.entryApMaterno.insert(0, self.ApMaterno)
            self.entryDNI.insert(0, self.DNI)
            self.entryFNacimiento.insert(0, self.FNacimiento)
            self.entryEdad.insert(0, self.Edad)
            self.entryprepagaOS.insert(0, self.prepagaOS)
            self.entryNprepagaOS.insert(0, self.NprepagaOS)
            self.entrycorreo.insert(0, self.correo)
            self.entrytelefono.insert(0, self.telefono)
            self.entryAlergia.insert(0, self.Alergia)
            self.entryMedActual.insert(0, self.MedActual)
            self.entryAPPCli.insert(0, self.APPCli)
            self.entryAPPQx.insert(0, self.APPQx)

        except:
            title = 'Editar Paciente'
            mensaje = 'ERROR al Editar Registro Pte'
            messagebox.showerror(title, mensaje)
    
    def eliminarDatoPaciente(self):
        try:
            # Obtener el ID del paciente seleccionado
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Registro Paciente'
            mensaje = 'NO se pudo eliminar Registro'
            messagebox.showinfo(title, mensaje)