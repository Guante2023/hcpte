import tkinter as tk
from paciente.gui import Frame

def main():
    root = tk.Tk()
    root.title("Registro de Pacientes")
    root.resizable(0, 0)

    frame = Frame(root)
    #frame.pack()  # Pack the frame to make it visible

    root.mainloop()  # Use root.mainloop() to start the Tkinter event loop

if __name__ == "__main__":
    main()
