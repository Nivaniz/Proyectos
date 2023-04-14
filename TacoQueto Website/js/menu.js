/**
 * Selecciona el botón hamburguesa y el menú de navegación y añade un listener para mostrar/ocultar el menú.
 */
const hamburguer = document.querySelector('.hamburguer')
const menu = document.querySelector('.menu-navegacion')

hamburguer.addEventListener('click', ()=>{
    menu.classList.toggle("spread")
})

/**
 * Añade un listener en la ventana para cerrar el menú si se hace clic fuera del menú o del botón hamburguesa.
 * @param {Event} e - El evento de clic en la ventana.
 */
window.addEventListener('click', e =>{
    if(menu.classList.contains('spread') 
        && e.target != menu && e.target != hamburguer){
        console.log('cerrar')
        menu.classList.toggle("spread")
    }
})
