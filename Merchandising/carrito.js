document.addEventListener('DOMContentLoaded', mostrarCarrito);
        // Función para mostrar los producto del carrito en la página del carrito
        function mostrarCarrito() {
            let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
            let listaCarrito = document.getElementById('lista-carrito');

            listaCarrito.innerHTML = '';
            carrito.forEach((producto, index) => {
                let li = document.createElement('li');
                li.textContent = `${producto.nombre} - $${producto.precio}`;
                
                // Botón para borrar el producto del carrito
                let botonBorrar = document.createElement('button');
                botonBorrar.textContent = 'Borrar';
                botonBorrar.addEventListener('click', () => {
                    borrarProducto(index);
                });
                li.appendChild(botonBorrar);
                
                listaCarrito.appendChild(li);
            });
        }

        // Función para borrar un producto del carrito

        function borrarProducto(index) {
            let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
            carrito.splice(index, 1);
            localStorage.setItem('carrito', JSON.stringify(carrito));
            mostrarCarrito();
        }

        // Función para completar la compra y variar el carrito
        function completarCompra(){
            //pueden agregar cualquier lógica adicional que deseen para procesar la compra
            alert('¡Compra completada con éxito! Gracias por su compra.');
            localStorage.removeItem('carrito'); // Vaciar el carrito
            mostrarCarrito(); // Actualizar la lista del carrito (se mostrará vacía)
        }