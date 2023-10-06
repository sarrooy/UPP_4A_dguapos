

# https://www.tutorialspoint.com/tcl-tk/tk_widgets_overview.htm
## link de messageBox
#https://www.tutorialspoint.com/python/tk_messagebox.htm

from tkinter import *
from tkinter import messagebox

#genero estructura
window = Tk()
### area de funciones y proyecto
window.title("aplicacion para Mostrar mensajes")
window.configure(background='ghost white')
window.geometry('200x300')

#area de funciones
def messageINFO():
    messagebox.showinfo("ventana de info", "aqui la info al usuario")
    
def messageYESNOCANCEL():
    messagebox.askyesnocancel("ventana de preguntas", "selecciona tu opcion")

#defino componentes
boton_INFO = Button(window, text="mostrar info", command= messageINFO)
boton_YESNOCANCEL = Button(window, text="mostrar YESNOCANCEL", command= messageYESNOCANCEL)

#defino LAYOUT = ORGANIZACION
boton_INFO.pack()
boton_YESNOCANCEL.pack()

###termina area de ventana
window.mainloop()