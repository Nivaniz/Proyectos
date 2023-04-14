/**
 * Guarda la posición actual del scroll
 * @type {number}
 */
let ubicacionPrincipal = window.pageYOffset; //0

// Inicializa AOS
AOS.init();

/**
 * Escucha el evento scroll y oculta o muestra la barra de navegación dependiendo de la dirección del scroll
 */
window.addEventListener("scroll", function(){
    /**
     * Guarda la posición actual del scroll
     * @type {number}
     */
    let desplazamientoActual = window.pageYOffset; //180

    if(ubicacionPrincipal >= desplazamientoActual){ // 200 > 180
        // Si el scroll es hacia arriba, muestra la barra de navegación
        document.getElementsByTagName("nav")[0].style.top = "0px"
    }else{
        // Si el scroll es hacia abajo, oculta la barra de navegación
        document.getElementsByTagName("nav")[0].style.top = "-100px"
    }

    // Actualiza la ubicación principal con la posición actual del scroll
    ubicacionPrincipal= desplazamientoActual; //200
});

/**
 * Selecciona los enlaces de la barra de navegación y el botón de hamburguesa
 * @type {NodeList}
 */
let enlacesHeader = document.querySelectorAll(".enlaces-header")[0];
let hamburguer = document.querySelectorAll(".hamburguer")[0];

/**
 * Variable booleana para controlar el estado del menú
 * @type {boolean}
 */
let semaforo = true;

/**
 * Escucha el evento click del botón de hamburguesa y muestra u oculta el menú
 */
hamburguer.addEventListener("click", function(){
    if(semaforo){
        // Si el menú está oculto, cambia el color del botón de hamburguesa a blanco
        document.querySelectorAll(".hamburguer")[0].style.color ="#fff";
        semaforo= false;
    }else{
        // Si el menú está visible, cambia el color del botón de hamburguesa a negro
        document.querySelectorAll(".hamburguer")[0].style.color ="#000";
        semaforo= true;
    }

    // Muestra u oculta el menú
    enlacesHeader.classList.toggle("menudos")
});
