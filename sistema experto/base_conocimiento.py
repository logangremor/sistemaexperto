import json

def Obtener_respuesta(r1,r2,r3,r4, prop):
        re1 = ""
        re2 = ""
        re3 = ""
        re4 = ""
        #Define el valor que tomara la primera pregunta
        if r1==1:
            re1 = "1"
        elif r1==2:
            re1 = "2-3"
        elif r1==3:
            re1 = "4 o más"
            
        #Define el valor que tomara la segunda pregunta
        if r2==1:
            re2 = "6-11"
        elif r2==2:
            re2 = "12-18"
        elif r2==3:
            re2 = "19-26"
        elif r2==4:
            re2 = "27 o más"
            
        #Define el valor que tomara la tercera pregunta
        if r3==1:
            re3 = "no"
        elif r3==2:
            re3 = "Discapacidad Fisica"
        elif r3==3:
            re3 = "Discapacidad sensorial"
        elif r3==4:
            re3 = "Discapacidad cognitiva"
            
        #Define el valor que tomara la cuarta pregunta
        if r4==1:
            re4 = "Escuela"
        elif r4==2:
            re4 = "Casa"
        elif r4==3:
            re4 = "Patio"
        
        Datos = ""
        # ruta = "./Base_Conocimientos.json"
        with open("./Base_Conocimientos.json", encoding='utf8') as contenido:
            conocimientos = json.load(contenido)
            for conocimiento in conocimientos:
                if re1==conocimiento.get('Pesonas') and re2==conocimiento.get('Edad') and re3==conocimiento.get('Discapacidad') and re4==conocimiento.get('Lugar'):
                    # return conocimiento.get(prop)
                    Datos=Datos + "\n\n" + conocimiento.get(prop)

            if(Datos == "" or Datos=="\n\n"):
                Datos = "No existe respuesta en la base de conocimiento"
        contenido.close()
        
        return Datos
    
    
def Obtener_Imagen(r1,r2,r3,r4, prop):
        re1 = ""
        re2 = ""
        re3 = ""
        re4 = ""        
    
        #Define el valor que tomara la primera pregunta
        if r1==1:
            re1 = "1"
        elif r1==2:
            re1 = "2-3"
        elif r1==3:
            re1 = "4 o más"
            
        #Define el valor que tomara la segunda pregunta
        if r2==1:
            re2 = "6-11"
        elif r2==2:
            re2 = "12-18"
        elif r2==3:
            re2 = "19-26"
        elif r2==4:
            re2 = "27 o más"
            
        #Define el valor que tomara la tercera pregunta
        if r3==1:
            re3 = "no"
        elif r3==2:
            re3 = "Discapacidad Fisica"
        elif r3==3:
            re3 = "Discapacidad sensorial"
        elif r3==4:
            re3 = "Discapacidad cognitiva"
            
        #Define el valor que tomara la cuarta pregunta
        if r4==1:
            re4 = "Escuela"
        elif r4==2:
            re4 = "Casa"
        elif r4==3:
            re4 = "Patio"        
        
        Datos = ""
        # ruta = "./Base_Conocimientos.json"
        with open("./Base_Conocimientos.json", encoding='utf8') as contenido:
            conocimientos = json.load(contenido)
            for conocimiento in conocimientos:
                if re1==conocimiento.get('Personas') and re2==conocimiento.get('Edad') and re3==conocimiento.get('Discapacidad') and re4==conocimiento.get('Lugar'):
                    # return conocimiento.get(prop)
                    Datos=Datos+conocimiento.get(prop)+" "
            if(Datos=="" or Datos==" "):
                Datos="./juegos/0.png"
        contenido.close()
        
        return Datos
                
                
def Cambiar_respuesta(r1,r2,r3,r4, res, des):
        re1 = ""
        re2 = ""
        re3 = ""
        re4 = ""        
    
        #Define el valor que tomara la primera pregunta
        if r1==1:
            re1 = "1"
        elif r1==2:
            re1 = "2-3"
        elif r1==3:
            re1 = "4 o más"
            
        #Define el valor que tomara la segunda pregunta
        if r2==1:
            re2 = "6-11"
        elif r2==2:
            re2 = "12-18"
        elif r2==3:
            re2 = "19-26"
        elif r2==4:
            re2 = "27 o más"
            
        #Define el valor que tomara la tercera pregunta
        if r3==1:
            re3 = "no"
        elif r3==2:
            re3 = "Discapacidad Fisica"
        elif r3==3:
            re3 = "Discapacidad sensorial"
        elif r3==4:
            re3 = "Discapacidad cognitiva"
            
        #Define el valor que tomara la cuarta pregunta
        if r4==1:
            re4 = "Escuela"
        elif r4==2:
            re4 = "Casa"
        elif r4==3:
            re4 = "Patio"   
        
        clave = 0     
        
        # ruta = "./Base_Conocimientos.json"
        with open("./Base_Conocimientos.json","r+", encoding='utf8') as contenido:
            conocimientos = json.load(contenido)
            
            Tm = (len(conocimientos)+1)
            
            for conocimiento in conocimientos:
                
                if re1==conocimiento.get('Personas') and re2==conocimiento.get('Edad') and re3==conocimiento.get('Discapacidad') and re4==conocimiento.get('Lugar'):
                    # js = json.loads(contenido)
                    # conocimiento.get('Descripcion') = "Pruba"
                    # conocimientos[clave]["Respuesta"] = res
                    # conocimientos[clave]["Descripcion"] = des

                    clave=+1

            Img = "./juegos/"+str(Tm)+".png"
            w = {
                "Personas": re1,
                "Edad": re2,
                "Discapacidad": re3,
                "Lugar": re4,
                "Respuesta": res,
                "Descripcion": des,
                "Imagen": Img
                }  
            conocimientos.append(w)   
            with open("./Base_Conocimientos.json","w", encoding='utf8') as cambio:
                json.dump(conocimientos, cambio, indent=1)
                    
                    # json.dump(conocimientos,conocimiento.get('Descripcion'))
                    # print(conocimiento.get('Descripcion'))
        contenido.close()
