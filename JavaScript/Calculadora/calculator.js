function setResult(value) {
    document.getElementById('result').innerHTML = value;
}
function getResult() {
    return(document.getElementById('result').innerHTML);
}
function add(key) { 
    var result = getResult();
    if (result!='0' || isNaN(key)) setResult(result + key);
    else setResult(key);
}
function calc() {
    var result = eval(getResult()); 
    setResult(result);
}
function del() { 
    setResult(0);
}

//SetResult(): Actualiza la pantalla de la calculadora poniendo el valor que se pase como parámetro.
//getResult(): Recoge el valor del último resultado obtenido, o de la expresión matemática que se debe calcular, y que se está visualizando en la pantalla de la calculadora.
//add(): Añade a la pantalla la tecla pulsada (por ejemplo, el dígito o la operación a realizar). Si la pantalla ya contiene algún dato o la tecla que se pulsa no es un dígito, el carácter de la tecla pulsada se añadirá a la pantalla. En caso contrario (por ejemplo, si la pantalla está a cero, y se pulsa otro dígito), el contenido de la pantalla se reemplazará con la tecla pulsada.
//calc(): Realiza el cálculo de la expresión que se encuentre en la pantalla (utilizando la función eval()), y escribe el resultado.
//del(): Pone a cero el contenido de la pantalla de la calculadora.