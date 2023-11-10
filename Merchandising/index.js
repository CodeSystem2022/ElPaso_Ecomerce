function agregarAlCarrito(nombre, precio){
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.push({nombre, precio});
    localStorage.setItem('carrito', JSON.stringify(carrito));
    alert(`El producto "${nombre}" se agregó al carrito`)
  }