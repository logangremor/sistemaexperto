from tkinter import *
from PIL import Image, ImageTk
import interfazexperto as interfaz_experto
import json
from base_conocimiento import Obtener_respuesta
from base_conocimiento import Obtener_Imagen
 
class InterfazUsuario(Tk):
    def __init__(self):
        #SE CREA UNA VENTANA NUEVA
        super().__init__()
        self.iconbitmap('./img/pelota.ico')
        self.title("Interfaz de usuario")
        self.geometry('700x700')

        #ATRIBUTOS
        # self.grid(column=0, row=0)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        self.config(bd=10, relief="groove",bg="white")

        #TITULO
        self.lblTitulo= Label(self)
        self.lblTitulo.grid(row=0, column=1, columnspan=6)
        imgTitulo = Image.open("./img/Titulo.png")
        imgTitulo.thumbnail(size=(550,120))
        tituloImg = ImageTk.PhotoImage(imgTitulo)
        self.lblTitulo.configure(image= tituloImg, bg="white")
        self.lblTitulo.image=tituloImg

        #VARIABLES PARA BUSCAR LA RESPUESTA
        self.selec = IntVar()
        self.selec2 = IntVar()
        self.selec3 = IntVar()
        self.selec4 = IntVar()

        self.espacio = Label(self, text=" ")
        self.espacio.config(font=('Arial', 15, "bold", ),bg="white")
        self.espacio.grid(row=1)

        # PREGUNTA 1
        self.lbl1 = Label(self, text="Personas")
        self.lbl1.config(font=('Arial', 15, "bold", ),bg="lightblue")
        self.lbl1.grid(row=2,column=1, padx=5, pady=5, sticky=W)
        radio1 = Radiobutton(self, text="1 ", font=('Arial', 13, "bold"), value=1, variable=self.selec,bg="white").grid(row=3,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        radio2 = Radiobutton(self, text="2-3", font=('Arial', 13, "bold"), value=2, variable=self.selec,bg="white").grid(row=4,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        radio3 = Radiobutton(self, text="4 o más", font=('Arial', 13, "bold"), value=3, variable=self.selec,bg="white").grid(row=5,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        
        #PREGUNTA 2
        self.lbl2 = Label(self, text="Edad")
        self.lbl2.config(font=('Arial', 15, "bold"),bg="lightblue")
        self.lbl2.grid(row=2,column=3, padx=5, pady=5, sticky=W)
        radio4 = Radiobutton(self, text="6-11", font=('Arial', 13, "bold"), value=1, variable=self.selec2,bg="white").grid(row=3,column=3, columnspan=2, padx=5, pady=5, sticky=W)
        radio5 = Radiobutton(self, text="12-18", font=('Arial', 13, "bold"), value=2, variable=self.selec2,bg="white").grid(row=4,column=3, columnspan=2, padx=5, pady=5, sticky=W)
        radio6 = Radiobutton(self, text="14-26", font=('Arial', 13, "bold"), value=13, variable=self.selec2,bg="white").grid(row=5,column=3, columnspan=2, padx=5, pady=5, sticky=W)
        radio7 = Radiobutton(self, text="27 o más", font=('Arial', 13, "bold"), value=13, variable=self.selec2,bg="white").grid(row=5,column=3, columnspan=2, padx=5, pady=5, sticky=W)

        #PREGUNTA 3
        self.lbl3 = Label(self, text="Persona Especial")
        self.lbl3.config(font=('Arial', 15, "bold"),bg="lightblue")
        self.lbl3.grid(row=7,column=1, padx=5, pady=5, sticky=W)
        radio8 = Radiobutton(self, text="No", font=('Arial', 13, "bold"), value=1, variable=self.selec3,bg="white").grid(row=8,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        radio9 = Radiobutton(self, text="Discapacidad física", font=('Arial', 13, "bold"), value=2, variable=self.selec3,bg="white").grid(row=9,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        radio10 = Radiobutton(self, text="Discapacidad sensorial", font=('Arial', 13, "bold"), value=3, variable=self.selec3,bg="white").grid(row=10,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        radio11 = Radiobutton(self, text="Discapacidad cognitiva", font=('Arial', 13, "bold"), value=3, variable=self.selec3,bg="white").grid(row=11,column=1, columnspan=2, padx=5, pady=5, sticky=W)
        
        #PREGUNTA 4
        self.lbl4 = Label(self, text="Lugar")
        self.lbl4.config(font=('Arial', 15, "bold"),bg="lightblue")
        self.lbl4.grid(row=7,column=3, padx=5, pady=5, sticky=W)
        radio12 = Radiobutton(self, text="Escuela", font=('Arial', 13, "bold"), value=1, variable=self.selec4,bg="white").grid(row=8,column=3, columnspan=2, padx=5, pady=5, sticky=W)
        radio13 = Radiobutton(self, text="Casa", font=('Arial', 13, "bold"), value=2, variable=self.selec4,bg="white").grid(row=9,column=3, columnspan=2, padx=5, pady=5, sticky=W)
        radio14 = Radiobutton(self, text="Patio", font=('Arial',13, "bold"), value=3, variable=self.selec4,bg="white").grid(row=10,column=3, columnspan=2, padx=5, pady=5, sticky=W)

        #BOTON DE RESPUESTA Y SU RESPECTIVO DESPLIEGUE 
        self.lbl5 = Button(self, text="RESPUESTA", command= self.respuesta, bg="green")
        self.lbl5.config(font=('Arial', 11, "bold"))
        self.lbl5.place(x=400,y=160, height=40, width=210)
        #LABEL DE LA RESPUESTA (TEXTO)
        self.lbl6 = Label(self, text=" ")
        self.lbl6.config(font=('helvetica', 12), wraplength=200, bg="lightgreen")
        self.lbl6.place(x=400,y=200, height=100, width=210)

        #LABEL DE LA IMAGEN
        self.lbl7 = Label(self, text="IMAGEN")
        self.lbl7.config(font=('helvetica',13, "bold"), bg="orange")
        self.lbl7.place(x=400,y=310, height=40, width=210)

        # BOTONES DE REGRESAR Y DE EXPLICACION
        b = Button(self, text="EXPLICACION", command=self.explicacion)
        b.config(font=('Arial', 11, "bold"), bg="blue", fg="white", relief=RAISED)  # bg = color de fondo , fg = color de texto
        b.place(x=10,y=550, height=40, width=180)

        # b2 = Button(self, text="Cambiar respuesta", command=interfaz_experto.InterfazExperto)
        self.b2 = Button(self)
        self.b2.config(font=('Arial', 11, "bold"), bg="red", wraplength=80)
        
        # self.explicacion()

    #CODIGO NUEVOOO
    def respuesta(self):

        radio1 = self.selec.get()
        radio2 = self.selec2.get()  
        radio3 = self.selec3.get()  
        radio4 = self.selec4.get()

        if(radio1!=0 and radio2!=0 and radio3!=0 and radio4!=0):
            print()
            res = Obtener_respuesta(radio1, radio2, radio3, radio4, 'Respuesta')
            # print(res+"-d-d-d-d--d-d-d--dd-d-")
            if(str(res)=="\n\n"):
                res = "No existe respuesta agregue una"
                self.b2.configure(text="AGREGAR JUEGO", command=interfaz_experto.InterfazExperto)
                self.b2.place(x=100,y=500, height=40, width=210)
        else:
            res = "No selecciono ninguna respuesta"
        
        

        self.lbl6.config(text=res)

        # LABEL DE DONDE SALE LA IMAGEN
        # self.lbl8= Label(self)
        # self.lbl8.grid(row=21, column=1)
        
        resimagen=""
        resimagen = Obtener_Imagen(radio1, radio2, radio3, radio4, 'Imagen')
        Info = resimagen.split(' ')
        cont = 0
        for Dat in Info:
            if (Dat!=""or Dat != " "):
                 #inserta imagen
                if(cont == 0):
                    
                    self.lbl8= Label(self)
                    self.lbl8.place(x=420,y=350)
                    img = Image.open(Dat)
                    img.thumbnail(size=(165,165))
                    img1 = ImageTk.PhotoImage(img)
                    self.lbl8.configure(image= img1)
                    self.lbl8.image=img1
                elif(cont == 1):
                    self.lbl9= Label(self)
                    self.lbl9.place(x=400,y=350)
                    img = Image.open(Dat)
                    img.thumbnail(size=(165,165))
                    img1 = ImageTk.PhotoImage(img)
                    self.lbl9.configure(image= img1)
                    self.lbl9.image=img1
                elif(cont == 2):
                    self.lb21= Label(self)
                    self.lb21.place(x=400,y=350)
                    img = Image.open(Dat)
                    img.thumbnail(size=(165,165))
                    img1 = ImageTk.PhotoImage(img)
                    self.lb21.configure(image= img1)
                    self.lb21.image=img1
                elif(cont == 3):
                    self.lb22= Label(self)
                    self.lb22.place(x=400,y=350)
                    img = Image.open(Dat)
                    img.thumbnail(size=(165,165))
                    img1 = ImageTk.PhotoImage(img)
                    self.lb22.configure(image= img1)
                    self.lb22.image=img1
                
                cont+=1
                
                print("------------->"+Dat+"-------------->")
          

       

        self.b2.configure(text="AGREGAR JUEGO", command=interfaz_experto.InterfazExperto, fg="white",)
        self.b2.place(x=200,y=550, height=40, width=180)

    # METODO DONDE OBTIENE EXPLICACION
    def explicacion(self):
        v2 = Toplevel(self)
        v2.iconbitmap('./img/pelota.ico')
        v2.title("Explicación")
        v2.geometry("400x400")
        v2.config(bd=10, relief="groove", bg="white")

        ancho_ventana = 500
        alto_ventana = 220
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        v2.geometry(posicion)

        tex = Label(v2, text=" ", wraplength=500, font=('Arial',11), bg="white") # Aqui poner solo la variable que tiene la explicación
        tex.pack(pady=10)
        salir = Button(v2, font=("Arial",11, "bold"), text="VOLVER",bg="red", fg="white", command=v2.destroy)
        salir.place(x=10,y=140, height=40, width=100)

        radio1 = self.selec.get()
        radio2 = self.selec2.get()  
        radio3 = self.selec3.get()  
        radio4 = self.selec4.get()
         
        res = ""
        res = Obtener_respuesta(radio1, radio2, radio3, radio4, 'Descripcion')

        tex.config(text=res)