#Librerias 

from tkinter import *
import tkinter
import requests

#Configuracion de la Ventana

ventana = tkinter.Tk()
ventana.title ("Weather Finder")
ventana.iconbitmap ('C:\\Users\\calis\\OneDrive\\Escritorio\\UCASAL\\1er Año\\Segundo Semestre\\Introduccion en Informatica\\Codigos\\App Oficial\\iconoapp3.ico')
ventana.geometry ("350x600")
ventana.resizable (False,False)


bg = PhotoImage(file = 'C:\\Users\\calis\\OneDrive\\Escritorio\\UCASAL\\1er Año\\Segundo Semestre\\Introduccion en Informatica\\Codigos\\App Oficial\\fondoapp1.png') 
canvas1 = Canvas(ventana, width = 350, height = 600) 
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#Comienzo del codigo

def mostrar_respuesta(clima):
    try: 
        nombre_cuidad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]
        humtxt= ("Porcentaje de Humedad")
        hum = clima["main"]["humidity"],("%")  

        cuidad["text"] = nombre_cuidad
        temperatura ["text"] = str(int(temp)) + "°C"
        descripcion ["text"] = desc
        humedadtext["text"] = humtxt
        humedad ["text"] = hum
     
    except:
        cuidad["text"] = "No hay resultado"
        temperatura ["text"] = ""
        descripcion ["text"] = ""
        humedadtext["text"] = ""
        humedad ["text"] = ""     

def clima_JSON(ciudad):
    try:
        API_key = "54f30a655f8f6b347eae6fc0eceb6c4f"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parametros)
        clima= response.json()
        mostrar_respuesta(clima)

    except:
        cuidad["text"] = "Error sin internet"

#Interfaz de la Ventana

etxt=tkinter.Label(ventana, font=("Helvetica", 20, "normal"),text='Buscar Ciudad',bg= '#303030',fg='white')
etxt_canvas = canvas1.create_window(90,30,anchor="nw",window=etxt)

textocuidad = tkinter.Entry(ventana, font=("Helvetica", 20, "normal"), justify="center")
textocuidad_canvas = canvas1.create_window(25,80,anchor="nw",window=textocuidad)

obtenerclima=tkinter.Button(ventana, text="Obtener Clima", font=("Helvetica", 10, "normal"), command= lambda: clima_JSON(textocuidad.get()))
obtenerclima_canvas = canvas1.create_window(125,130,anchor="nw",window=obtenerclima)

#Interfaz del resultado de la busqueda

cuidad=tkinter.Label(font=("Helvetica", 30, "normal"),bg= '#303030',fg='white')
ciudad_canvas = canvas1.create_window(25,180,anchor="nw",window=cuidad)

temperatura=tkinter.Label(font=("Helvetica", 50, "normal"),bg= '#303030',fg='white')
temperatura_canvas = canvas1.create_window(25,250,anchor="nw",window=temperatura)

descripcion=tkinter.Label(font=("Helvetica", 30, "normal"),bg= '#303030',fg='white')
decripcion_canvas = canvas1.create_window(25,350,anchor="nw",window=descripcion)

humedadtext=tkinter.Label(font=("Helvetica", 15, "normal"),bg= '#303030',fg='white')
humedad_canvas = canvas1.create_window(25,420,anchor="nw",window=humedadtext)

humedad=tkinter.Label(font=("Helvetica", 50, "normal"),bg= '#303030',fg='white')
humedad_canvas = canvas1.create_window(25,460,anchor="nw",window=humedad)

ventana.mainloop()