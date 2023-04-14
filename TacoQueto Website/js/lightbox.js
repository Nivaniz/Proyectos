// Seleccionamos todos los elementos con la clase 'img-galeria'
const imagenes = document.querySelectorAll('.img-galeria')
// Seleccionamos el elemento con la clase 'agregar-imagen'
const imagenLight = document.querySelector('.agregar-imagen');
// Seleccionamos el elemento con la clase 'imagen-light'
const contenedorLight = document.querySelector('.imagen-light')
// Seleccionamos el elemento con la clase 'close'
const closeLight = document.querySelector('.close')

// Iteramos sobre cada imagen y le añadimos un evento click que llama a la función aparecerImagen
imagenes.forEach(imagen => {
    imagen.addEventListener('click',()=>{
        aparecerImagen(imagen.getAttribute('src'));
    })
});

// Añadimos un evento click al contenedor de la imagen light
contenedorLight.addEventListener('click',(e)=>{
    // Si el elemento clickeado no es la imagen light, es decir, es el contenedor o el botón de cerrar, entonces se oculta la imagen light
    if(e.target !== imagenLight){
        contenedorLight.classList.toggle('show')
        imagenLight.classList.toggle('showImage')
        hamburguer.style.opacity = '1';
    }
})

// Función que muestra la imagen light
const aparecerImagen = (imagen)=>{
    // Cambiamos la imagen del src de la imagen light por la imagen clickeada
    imagenLight.src = imagen;
    // Mostramos el contenedor y la imagen light
    contenedorLight.classList.toggle('show')
    imagenLight.classList.toggle('showImage')
    // Escondemos el botón de hamburguesa
    hamburguer.style.opacity = '0';
}