# Creamos la clase productos y la coleccion que guardaremos en nuestra base de datos
class Product:
    def __init__(self, name, lastName, edad, dni, email, pais, description, legajo):                                               # VAMOS A HACER UNOS CAMBIOS
        self.name = name
        self.lastName = lastName
        self.edad = edad
        self.dni = dni
        self.email = email
        self.pais = pais
        self.description = description                                     #HACEMOS CAMBIOS
        self.legajo = legajo


# Creamos la funcion para crear la coleccion o el documento que se va a guardar en la base de datos

    def toDBCollection(self):
        return{
            'name': self.name,
            'lastName': self.lastName,
            'edad': self.edad,
            'dni': self.dni,
            'email': self.email,
            'pais': self.pais,
            'description': self.description,
            'legajo': self.legajo
            
            
        }
    

     