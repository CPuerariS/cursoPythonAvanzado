import json

#with open ("user.json", "r") as archivo:
#    data = json.load(archivo)

with open ("user.json", "w") as archivo:
    data = {
        "nombre": "Ana",
        "edad": 28,
        "ciudad": "Buenos Aires",
        "correo": "ana@gmail.com",
        "hobbies": [
        "correr", 
        "leer libros"]
    }
    json.dump(data, archivo, indent=4)