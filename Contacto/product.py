# Creamos la clase productos y la coleccion que guardaremos en nuestra base de datos
class Product:
    def __init__(self, name, lastName, dni, email, pais, message, orden):                                               # VAMOS A HACER UNOS CAMBIOS
        self.name = name
        self.lastName = lastName
        self.dni = dni
        self.email = email
        self.pais = pais
        self.message = message                                     #HACEMOS CAMBIOS
        self.orden = orden


# Creamos la funcion para crear la coleccion o el documento que se va a guardar en la base de datos

    def toDBCollection(self):
        return{
            'name': self.name,
            'lastName': self.lastName,
            'dni': self.dni,
            'email': self.email,
            'pais': self.pais,
            'message': self.message,
            'orden': self.orden
            
            
        }
    

     