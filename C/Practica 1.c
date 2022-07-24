#include <stdio.h>
#include <stdlib.h>

int main (int argc,char*argv[]){
	//declaración de variables
	
	int numero1,numero2;
	float numero3;
	char letra;
	char palabra[5];
	
	//recolectar información
	printf("\n Escriba el valor de numero 1:");
	scanf("%d",&numero1);
	fflush (stdin);
	printf("\n Escriba el valor de numero 2:");
	scanf("%d",&numero2);
	fflush (stdin);
	printf("\n Escriba el valor de numero 3 de decimal:");
	scanf("%f",&numero3);
	fflush (stdin);
	printf("\n Escriba el valor de letra:");
	scanf("%s",&letra);
	fflush (stdin);
	printf("\n Escriba el valor de palabra:");
	scanf("%s",&palabra);
	fflush (stdin);
	//mostrar resultado
	
	printf("\n El valor introducido de numero1 es: %d",numero1);
	printf("\n El valor introducido de numero2 es: %d",numero2);
	printf("\n El valor introducido de numero3 de decimal es: %f",numero3);
	printf("\n El valor introducido de letra es: %c",letra);
	printf("\n El valor introducido de palabra es: %s",&palabra);
	
	return 0;
}
