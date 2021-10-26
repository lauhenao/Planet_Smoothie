/* CARRITO DE COMPRA */
const cards = document.getElementById('cards');
const items = document.getElementById('items');
const footer = document.getElementById('footer');
const templateCard = document.getElementById('template-card').content;
const templateFooter = document.getElementById('template-footer').content;
const temaplateCarrito = document.getElementById('template-carrito').content;
const fragment = document.createDocumentFragment()
let carrito = {};



document.addEventListener('DOMContentLoaded', ()=>{
    fetchData();
      if(localStorage.getItem('carrito')){ //Sirve para cuando actualizemos no se borre el carrito, con esta función vamos a almacenarlo con el localStorage. Primero debemos saber donde lo vamos a almacenar, 
        carrito = JSON.parse(localStorage.getItem('carrito')) //Si en localStorage existe la colección llamada carrito la almacenamos con  getItem
        mostrarCarrito();
    } 
})

cards.addEventListener('click', e =>{ //Evento del botón, cuando de click agrega al carrito
    addCarrito(e) /* Con el (e) capuramos el elemento que querramos modificar */
})

items.addEventListener('click', (e) => {btnAccion(e)} );


const fetchData = async () =>{
    try {
        const res = await fetch('/static/js/api.json'); /* Con esto hacemos que el coódigo no se ejecute hasta que lea el .json ( podemos agregar la URL del DB) */
        const data = await res.json() /* Una vez lo leyó, con este await esperamos a que lea el json para poder seguir con el codigo */
        //console.log(data);
        

        pintarCards(data)
    } catch (error) {
        console.log(error)       
    }
}



const pintarCards = data => {
    data.forEach(producto => {
        //console.log(data)
        templateCard.querySelector('h2').textContent = producto.nombre
        templateCard.querySelector('h1').textContent = producto.precio
        templateCard.querySelector('h4').textContent = producto.info
        templateCard.querySelector('img').setAttribute('src',producto.img)
        templateCard.querySelector('.btn-dark').dataset.id = producto.id
        cards.className = 'productos'
        
        
        const clone = templateCard.cloneNode(true)
        fragment.appendChild(clone)
    });
    cards.appendChild(fragment)
}

const addCarrito = e =>{
    //console.log(e.target)

    //console.log(e.target.classList.contains('btn-dark'))
    if(e.target.classList.contains('btn-dark')){
        //console.log(e.target.parentElement); 
        setCarrito(e.target.parentElement);
    }
    e.stopPropagation();
}

const setCarrito = objeto => { 
    //onsole.log(objeto);
    const producto = {
        nombre: objeto.querySelector('h2').textContent,
        precio: objeto.querySelector('h1').textContent,
        id: objeto.querySelector('.btn-dark').dataset.id,
        //img: templateCard.querySelector('img').setAttribute('src',producto.img),
        cantidad: 1
        /* img: objeto.querySelector('img').setAttribute('src',producto.img), */
    }
    if(carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad + 1;/* Con esto sumamos las cantidades */
    }

    carrito[producto.id] = {...producto}
    mostrarCarrito();
    /* console.log(producto); */
}

const mostrarCarrito = () =>{
    //console.log(carrito)
    items.innerHTML = ''
    Object.values(carrito).forEach(producto => {

        temaplateCarrito.querySelector('th').textContent = producto.id,
        temaplateCarrito.querySelectorAll('td')[0].textContent = producto.nombre;
        temaplateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad;
        temaplateCarrito.querySelector('.btn-info').dataset.id = producto.id;
        temaplateCarrito.querySelector('.btn-danger').dataset.id = producto.id;
        temaplateCarrito.querySelector('span').textContent = producto.cantidad * producto.precio;

        const clone = temaplateCarrito.cloneNode(true);
        fragment.appendChild(clone)
        
    })
    items.appendChild(fragment)

    mostrarFooter()

    localStorage.setItem('carrito', JSON.stringify(carrito)) //LocalStorage guarda todo a string plano, por eso usamos Stringify
}
const mostrarFooter = () =>{ 
    footer.innerHTML =''
    if(Object.keys(carrito).length === 0){
        footer.innerHTML = ` <th scope="row" colspan="5">No hay Smoothie delicia :C</th>
        `
        return
    }

    const nCantidad = Object.values(carrito).reduce((acc, {cantidad}) => acc + cantidad, 0)
    const nPrecio = Object.values(carrito).reduce((acc, {cantidad, precio}) => acc + cantidad * precio, 0)
    
    templateFooter.querySelectorAll('td')[0].textContent = nCantidad;
    templateFooter.querySelector('span').textContent = nPrecio;

    const clone = templateFooter.cloneNode(true);
    fragment.appendChild(clone);
    footer.appendChild(fragment);

    const btnVaciar = document.getElementById('vaciar-carrito')
    btnVaciar.addEventListener('click', ()=> {
        carrito = {}
        mostrarCarrito()
    })
}

const btnAccion = e =>{
    //console.log(e.target)
    //acción de aumentar
    if(e.target.classList.contains('btn-info')){
        //console.log(carrito[e.target.dataset.id])
        //carrito[e.target.dataset.id]
        const producto = carrito[e.target.dataset.id]
        producto.cantidad++
        carrito[e.target.dataset.id] = {...producto}
        mostrarCarrito();
    }
    if(e.target.classList.contains('btn-danger')){
        const producto = carrito[e.target.dataset.id]
        producto.cantidad--
        mostrarCarrito();
        if(producto.cantidad === 0){
            delete carrito[e.target.dataset.id]
            mostrarCarrito();
        }
        
    }
    e.stopPropagation();
}



