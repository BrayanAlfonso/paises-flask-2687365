# Impotar las dependencias de flask

from flask import Flask, render_template



#Crear el objeto flask

app= Flask(__name__)

#Crear ruta de prueba
@app.route("/Hola")
def HolaMundo():
    return 'Hola Mundo Programador :D'

#Ruta De Paises 
@app.route("/paises")
def paises():
    userName="Juan Mecanico"
    Continentes=[
        {
        "Nombre": "America",
        "Poblacion": 1036900579,
        "Superficie" : "42549000km2" ,
        "No_Paises": 35,
        "paises":[
            {
                "nom":"Colombia",
                "mon":"COP",
                "cap":"Bogotá",
                "poblacion":"7.181 Millones"},
            {
                "nom":"Perú",
                "mon":"Sol",
                "cap":"Lima",
                "poblacion":"33,72 Millones"
                },
                
            {
                "nom":"Paraguay",
                "mon":"Guaraní",
                "cap":"Asunción",
                "poblacion":"6.704 Millones"},
            {
                "nom":"Chile",
                "mon":"CLP",
                "cap":"Santiago de Chile",
                "poblacion":"19.49 Millones"}

        ],
        "Densidad":"22,8 hab / km2"
            
        },
        
        {
        "Nombre": "Europa",
        "Poblacion": 747747395,
        "Superficie" : "10530751km2" ,
        "No_Paises":50 ,
        "paises":[
            {
                "nom":"Alemania",
                "mon":"Euro",
                "cap":"Berlín",
                "poblacion":"83,2 Millones"},
            {
                "nom":"Italia",
                "mon":"Euro",
                "cap":"Roma",
                "poblacion":"59,2 Millones"
            }
            # "Alemania",
            # "Italia"
        ],
        "Densidad": "71 hab / km2"
        },
        
        {
        "Nombre": "Asia",
        "Poblacion": 4598168800,
        "Superficie" : "44541138km2"  ,
        "No_Paises":51 ,
        "paises":[
            {
                 "nom":"Japon",
                "mon":"Yen",
                "cap":"Tokio",
                "poblacion":"125,7 Millones"},
            {
                 "nom":"Indonesia",
                "mon":"IDR",
                "cap":"Yakarta",
                "poblacion":"273,8 Millones"},
            {
                 "nom":"China",
                "mon":"Yuan",
                "cap":"Pekin",
                "poblacion":"1.412 Millones"
            }
            # "Japon",
            # "Indonesia",
            # "Hong Kong"
        ],
        "Densidad": "103,2 hab / km2"
        },
        
        {
        "Nombre": "Oceania",
        "Poblacion": 41117432,
        "Superficie" : "8542499km2" ,
        "No_Paises":15 ,
        "paises":[
            # "Nueva Zelanda",
            {
                 "nom":"Nueva Zelanda",
                "mon":"NZE",
                "cap":"Wellington",
                "poblacion":"5,123 Millones"
            }
        ],
        "Densidad" :"4.56 hab /km2"
        },
        {
        "Nombre": "Africa",
        "Poblacion": 1320000000,
        "Superficie" :"30221535km2"  ,
        "No_Paises": 54,
        "paises":[
            # "Sudafrica",
            # "Nigeria"
            {
                 "nom":"Sudafrica",
                "mon":"Rand",
                "cap":"Pretoira",
                "poblacion":"53,39 Millones"},
            
            {
                 "nom":"Nigeria",
                "mon":"Naira",
                "cap":"Abuya",
                "poblacion":"213,4 Millones"
            }
        ],
        "Densidad": "43,7 hab/ km2"
        }
    ]
    return render_template("paises.html", userName=userName,Continentes=Continentes) 
    
    