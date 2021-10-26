const contacto = {
    nombre: '',
    email: '',
    mensaje: ''
}

const nombre = document.querySelector('#nombre')
const email = document.querySelector('#email')
const mensaje = document.querySelector('#mensaje')
const formulario = document.querySelector('.formulario')

nombre.addEventListener('input', leerTexto);
email.addEventListener('input', leerTexto);
mensaje.addEventListener('input', leerTexto);
formulario.addEventListener('submit', (evento)=>{
    
    evento.preventDefault();

    const {nombre, email, mensaje} = contacto;

    if(document.querySelector('.error') === null && document.querySelector('.completo') === null){
        if(nombre ==='' || email.toLocaleLowerCase() ==='' || mensaje.toLocaleLowerCase() ===''){
            mostrarAlerta('Todos los campos deben ser obligatorios', true)
            return;
        }else{
            mostrarAlerta('Muchas gracias por contactarnos pronto uno de nuestros asesores se comuninicará contigo')
        }
    }
})

function leerTexto (e){
    contacto[e.target.id] = e.target.value;
}

function mostrarAlerta(mensaje, error = null){
    const alerta = document.createElement('P');
    alerta.textContent = mensaje;

    if(error){
        alerta.classList.add('error')
    }else{
        alerta.classList.add('completo')
    }

    formulario.appendChild(alerta);

    setTimeout(() => {
        alerta.remove()
    }, 5000);
    
}