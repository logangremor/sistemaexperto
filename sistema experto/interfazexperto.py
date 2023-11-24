import json
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps
from base_conocimiento import Cambiar_respuesta


class InterfazExperto(Toplevel):
    def __init__(self):
        #SE CREA UNA VENTANA NUEVA
        super().__init__()
        self.iconbitmap('./img/pelota.ico')
        self.title("Interfaz de usuario experto")
        self.resizable(width=False, height=False)

        #ATRIBUTOS
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(bd=10, relief="groove")

        #TITULO
        lbl = Label(self, text="Módulo de adiquisición de conocimiento")
        lbl.config(font=('Comic Sans MS', 15, "bold")) # Cambiar letra y color del texto
        lbl.place(x=28, y=0)

        #VARIABLES PARA BUSCAR LA RESPUESTA
        self.selec = IntVar()
        self.selec2 = IntVar()
        self.selec3 = IntVar()
        self.selec4 = IntVar()
        #ESPACIO VACIO 
        espacio = Label(self, text=" ")
        espacio.grid(row=0, column=0,columnspan=3, pady=10, sticky=SE)

        # PREGUNTA 1
        self.lbl1 = Label(self, text="Personas:")
        self.lbl1.config(font=('Arial', 11, "bold"))
        self.lbl1.grid(padx=10, row=1, sticky=E)
        radio1 = Radiobutton(self, text="1", font=('Arial', 10), value=1, variable=self.selec).grid(row=1, column=1, sticky=W)
        radio2 = Radiobutton(self, text="2-3", font=('Arial', 10), value=2, variable=self.selec).grid(row=2, column=1, sticky=W)
        radio3 = Radiobutton(self, text="4 o más", font=('Arial', 10), value=3, variable=self.selec).grid(row=3, column=1, sticky=W)
        
        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=5)

        #PREGUNTA 2
        self.lbl2 = Label(self, text="Edad:")
        self.lbl2.config(font=('Arial', 11, "bold"))
        self.lbl2.grid(padx=10, row=6, sticky=E)
        radio4 = Radiobutton(self, text="6-11", font=('Arial', 10), value=1, variable=self.selec2).grid(row=6, column=1, sticky=W)
        radio5 = Radiobutton(self, text="12-18", font=('Arial', 10), value=2, variable=self.selec2).grid(row=7, column=1, sticky=W)
        radio6 = Radiobutton(self, text="14-26", font=('Arial', 10), value=3, variable=self.selec2).grid(row=8, column=1, sticky=W)
        radio7 = Radiobutton(self, text="27 o más", font=('Arial', 10), value=4, variable=self.selec2).grid(row=8, column=1, sticky=W)
        
        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=8)

        #PREGUNTA 3
        self.lbl3 = Label(self, text="Persona Especial:")
        self.lbl3.config(font=('Arial', 11, "bold"))
        self.lbl3.grid(padx=10, row=9, sticky=E)
        radio8 = Radiobutton(self, text="No", font=('Arial', 10), value=1, variable=self.selec3).grid(row=9, column=1, sticky=W)
        radio9 = Radiobutton(self, text="Discapacidad física", font=('Arial', 10), value=2, variable=self.selec3).grid(row=10, column=1, sticky=W)
        radio10 = Radiobutton(self, text="Discapacidad sensorial", font=('Arial', 10), value=3, variable=self.selec3).grid(row=11, column=1, sticky=W)
        radio11 = Radiobutton(self, text="Discapacidad cognitiva", font=('Arial', 10), value=4, variable=self.selec3).grid(row=12, column=1, sticky=W)
        
        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=12)

        #PREGUNTA 4
        self.lbl4 = Label(self, text="Lugar:")
        self.lbl4.config(font=('Arial', 11, "bold"))
        self.lbl4.grid(padx=10, row=13, sticky=E)
        radio12 = Radiobutton(self, text="Escuela", font=('Arial', 10), value=1, variable=self.selec4).grid(row=13, column=1, sticky=W)
        radio13 = Radiobutton(self, text="Casa", font=('Arial', 10), value=2, variable=self.selec4).grid(row=14, column=1, sticky=W)
        radio14 = Radiobutton(self, text="Patio", font=('Arial', 10), value=3, variable=self.selec4).grid(row=15, column=1, sticky=W)
        

        #LABEL PARA RESPUESTA
        self.lbl5 = Label(self, text="Respuesta:")
        self.lbl5.config(font=('Arial', 11, "bold"))
        self.lbl5.grid(padx=15, row=17, pady=15, sticky=E)
        # PARA INSERTAR LA RESPUESTA
        self.lbl6 = Text(self, width=45, height=2)
        self.lbl6.config(font=('Arial', 9))
        self.lbl6.grid(row=17, column=1, columnspan=2, sticky=W)

        #LABEL PARA EXPLICACIÓN
        self.lbl7 = Label(self, text="Explicación:")
        self.lbl7.config(font=('Arial', 11, "bold"))
        self.lbl7.grid(padx=10, row=18, pady=5, sticky=E)
        # PARA INSERTAR EXPLICACION
        self.lbl8 = Text(self, width=45, height=5)
        self.lbl8.config(font=('Arial', 9))
        self.lbl8.grid(row=18, column=1, columnspan=2, sticky=W)


        #LABEL PARA IMAGEN
        self.lbl9 = Label(self, text="Imagen:")
        self.lbl9.config(font=('Arial', 11, "bold"))
        self.lbl9.grid(row=19, column=0, pady=15, padx=10, sticky=E)

        # BOTON PARA SUBIR IMAGEN
        self.lbl20= Button(self, text="Subir", command=self.browseFiles)
        self.lbl20.config(font=('Arial', 11, "bold"))
        self.lbl20.grid(row=19, column=1, sticky=W)

        # BOTONES DE REGRESAR Y GUARDAR
        b = Button(self, text="Guardar",command= self.Cambiar)
        b.config(font=('Arial', 11, "bold", "italic"), fg="blue")  # bg = color de fondo , fg = color de texto
        b.grid(row=20, column=0, sticky=E)

        b2 = Button(self, text="Regresar", command=self.destroy)
        b2.config(font=('Arial', 11, "bold"), fg="red")
        b2.grid(padx=60, pady=5, row=20, column=2)

    # METODO PARA SUBIR LA IMAGEN
    def browseFiles(self): 
        filename = filedialog.askopenfilename(initialdir = "/", 
                                            title = "Selecciona un archivo", 
                                            filetypes = (("Imagen png", "*.png*"), 
                                                         ("Imagen gif", "*.gif*"), 
                                                         ("Todos los archivos", "*.*")))
        
        with open("./Base_Conocimientos.json","r+", encoding='utf8') as contenido:
            conocimientos = json.load(contenido)
            
            Tm = (len(conocimientos)+1)
        
        Ruta = "./regalos/"+str(Tm)+".png"
        img = Image.open(filename)
        img.save(Ruta,'png')
        
        
        self.lbl20.configure(text="Archivo subido: "+filename)
        
    def Cambiar(self):

         radio1 = self.selec.get()
         radio2 = self.selec2.get()  
         radio3 = self.selec3.get()  
         radio4 = self.selec4.get()
         
         res = self.lbl6.get(0.1, "end-1c")
         des = self.lbl8.get(0.1, "end-1c") 

         cam = Cambiar_respuesta(radio1, radio2, radio3, radio4, res, des)