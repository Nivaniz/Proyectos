#include <stdio.h>

int main (void){
	// declaracion del arreglo
 int arreglo [8];
 int indice;
 
 //leer los elementos del arreglo
 for(indice=0;indice<8;indice++){
 	 printf("Dame el elemento %d :", indice);
 	 scanf("%d",&arreglo[indice]);
 	 
 }//cierre de for
 
 //impresion de un arreglo
 printf("\n El contenido del arreglo es \n");
 for(indice=0;indice<8;indice++){
  printf("\t\tElemento de %d: %d \n", indice, arreglo[indice]);
 }//fin de for 2
 
return 0;
}

 
 
