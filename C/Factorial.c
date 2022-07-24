#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char*argv[]){
int num,cont,fact;
  num=0;
  
  printf("Ingresa el número a calcular el factorial");
  scanf("%d",&num); // dato ingresasdo por el usuario
  cont=1; // inicializa el contador
 fact = 1; // inicializa el contador
 
 do {
fact= fact*cont;
 cont=cont+1;
 printf("\n Contador: %d",cont);
 printf("\n Acumulador %d",fact);
 }while (cont<num);
 
 printf("\n El factorial del numero: %d",num, "Es: %d",fact);
 	
return 0;
}

 
