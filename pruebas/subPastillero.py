import pyrebase
import time


#Creamos un while para que cada 10 seg publique la informacion en el formato correcto


def pastilleroLaura():
    #Laura
    print("Datos paciente Laura")

    pastilleroLau = db.child("BayTec").child("Laura").child("Pastillero").get().val()
    print(pastilleroLau)

    habitacionLau = db.child("BayTec").child("Laura").child("Habitacion").get().val()
    print(habitacionLau)

    horarioLau = db.child("BayTec").child("Laura").child("Horario").get().val()
    #Modificamos la varibale horarioLau para que nos la de en formato de lista ya accesible 
    horarioLau = horarioLau.translate({ord('['):None, ord(']'):None, ord('"'):None}) 
    horarioLau = horarioLau.split(',')
    print(horarioLau)
    return pastilleroLau, habitacionLau, horarioLau

#print("Data loaded from real time database")

def pastilleroAnthony():
    #Anthony
    print("Datos paciente Anthony")

    pastilleroAnth = db.child("BayTec").child("Anthony").child("Pastillero").get().val()
    print(pastilleroAnth)

    habitacionAnth = db.child("BayTec").child("Anthony").child("Habitacion").get().val()
    print(habitacionAnth)

    horarioAnth = db.child("BayTec").child("Anthony").child("Horario").get().val()
    horarioAnth = horarioAnth.translate({ord('['):None, ord(']'):None, ord('"'):None}) 
    horarioAnth = horarioAnth.split(',')
    print(horarioAnth)  
    return pastilleroAnth, habitacionAnth, horarioAnth

#print("Data loaded from real time database")

def pastilleroAmadeo():
    #Amadeo
    print("Datos paciente Amadeo")

    pastilleroAmad = db.child("BayTec").child("Amadeo").child("Pastillero").get().val()
    print(pastilleroAmad)

    habitacionAmad = db.child("BayTec").child("Amadeo").child("Habitacion").get().val()
    print(habitacionAmad)

    horarioAmad = db.child("BayTec").child("Amadeo").child("Horario").get().val()
    horarioAmad = horarioAmad.translate({ord('['):None, ord(']'):None, ord('"'):None}) 
    horarioAmad = horarioAmad.split(',')
    print(horarioAmad)
    return pastilleroAmad, habitacionAmad, horarioAmad

#print("Data loaded from real time database")


def pastilleroAlonso():
    #Alonso
    print("Datos paciente Alonso")

    pastilleroAlo = db.child("BayTec").child("Alonso").child("Pastillero").get().val()
    print(pastilleroAlo)

    habitacionAlo = db.child("BayTec").child("Alonso").child("Habitacion").get().val()
    print(habitacionAlo)

    horarioAlo = db.child("BayTec").child("Alonso").child("Horario").get().val()
    horarioAlo = horarioAlo.translate({ord('['):None, ord(']'):None, ord('"'):None}) 
    horarioAlo = horarioAlo.split(',')
    print(horarioAlo)
    return pastilleroAlo, habitacionAlo, horarioAlo

#print("Data loaded from real time database ")
      
config = {
  "apiKey": "AIzaSyBOSmtJEkga1km5itsEATqc8DJ0EuzKgBs",

  "authDomain": "baytec-833d3.firebaseapp.com",

  "databaseURL": "https://baytec-833d3-default-rtdb.firebaseio.com",

  "projectId": "baytec-833d3",

  "storageBucket": "baytec-833d3.appspot.com",

  "messagingSenderId": "73252566520",

  "appId": "1:73252566520:web:a6ae2120d12de826ef920d"

}

#create authetication
firebase = pyrebase.initialize_app(config)
#accesing database in firebase
db = firebase.database()

print("HOla")