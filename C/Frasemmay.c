#include <stdio.h>
#include <ctype.h>

#define TAMANO 30
/*leer una línea un texto en minúsculas y escribirla en mayúsculas */
int main(void){
	char Letras[TAMANO];
	int cont;
	
	//Leer línea
	printf("\t\t\tEscribe la frase a convertir:");
	 for(cont=0;cont<TAMANO; cont++){
	    Letras[cont]=getchar();
	}//fin de for
	//escribir la línea en mayúsculas
	 printf("\n\n\t\t\tLa frase en mayusculas es: \n");
	 for(cont=0;cont<TAMANO;++cont){
	 	putchar(toupper(Letras[cont]));
	 }//fin del segundo for
	 return 0;
}

