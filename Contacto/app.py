# Importamos el metodo random para generar auto-legajo 
import random
#Importamos las clases para enviar el email
import smtplib
from email.message import EmailMessage

from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, url_for)

import database as dbase
from product import Product

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

'''#Ruta home 2
@app.route('/')
def homeDos():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)
'''
# Legajo generado automaticamente

legajo = random.randint(2000, 4500)

#Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    lastName = request.form['lastName']
    edad = request.form['edad']
    dni = request.form['dni']
    email = request.form['email']
    pais = request.form['pais']
    description = request.form['description']

    if name and lastName and edad and dni and email and pais and description and legajo:
        product = Product(name, lastName, edad, dni, email, pais, description, legajo)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'lasName': lastName,
            'edad': edad,
            'dni': dni,
            'email': email,
            'pais': pais,
            'description' : description,
            'legajo': legajo
            
            
        })                                                                             # Alguno cambios
        return redirect(url_for('home'))
    else:
        return notFound()
    
    
    
        
        
# Envio de email confirmando suscripcion

remitente = "denismembrive4@gmail.com"
destinatario = "denismembrive@gmail.com"
mensaje = "¡Se ha registrado correctamente!"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "znvqcqmcqwkptdfe")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()











#Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    lastName = request.form['lastName']
    edad = request.form['edad']
    dni = request.form['dni']
    email = request.form['email']
    pais = request.form['pais']
    description = request.form['description']

    if name and lastName and edad and dni and email and pais and description:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name,'lastName' : lastName, 'edad' : edad, 'dni' : dni, 'email' : email, 'pais' : pais,  'description' : description, }})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(debug=True, port=4000)