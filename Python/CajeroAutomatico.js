//Excelente el curso
// Alvaro, Alexis y Beto!! Estoy comenzando a programar y me han traído mucha claridad acerca de los fundamentos esenciales de la programación!

let clave = 123456;
let saldo = 1000;
let usuario = "johan";

function validarUsuario(u, c) 
{
	if (u == usuario && c == clave)
	{
		return true
		return false
	}	
}

function login() 
{
	usuario = prompt("digite el usuario")
	clave = parseInt(prompt("digite la contraseña"));
	return validarUsuario(usuario, clave)
}

function retirar(valor) 
{
	if (valor > saldo)
	{
		return false , saldo
	}
	return true , saldo - valor
}

function depositar(valor)
{
	return true , saldo + valor
}

function accion(opcion) 
{
	if (opcion == 1)
	{
		valor = parseInt(prompt("digite el valor a depositar"))
			return depositar(valor)
	}

	if (opcion == 2) 
	{
		valor = parseInt(prompt("digite el valor a retirar"))
			return retirar(valor)
	}
	return false, saldo
}   

function ejecutar() 
{
	if (login() != true)
	{
		console.log("usuario o contraseña invalido")
			return
	}
	console.log("que desea hacer?")
	opcion = parseInt(prompt("1.depositar o 2.retirar"))
	let ok, saldo = accion(opcion)
	if (ok)
	{
		console.log("no se realizo la accion, saldo:", saldo);
	}
	else{
		console.log("accion realizada correctamente, saldo:", saldo);
	}
}
ejecutar() 