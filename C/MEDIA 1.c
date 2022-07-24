#include <stdio.h>
#include <stdlib.h>

//Para calcular la media de n numeros, después
//computar la desviación de cada numero
//respecto a la media

int main(int argc,char *argv[]){
	    
	    int n,cont;
	    float media,d,suma=0;
	    float lista[100];
	    
	    //Leer el valor de n
	    printf("\n¿Cuantos numeros para calcular la media?");
	    scanf("%d",&n);
	    printf("\n");
	    //leer los elementos y calcular la suma
	    for(cont=0;cont<n;++cont){
	    	printf("i=%d x=",cont+1);
	    	scanf("%f",&lista[cont]);
	    	suma+=lista[cont];
		}//fin de for
		//calcular la media y escribir la respuesta
		media=suma/n;
		printf("\nLa media es = %5.2f\n\n",media);
		
		//calcular y escribir las derviaciones
		for(cont=0; cont<n;++cont){
			d=lista[cont]-media;
			printf("i=%d \tx=%5.2f \td=%5.2f\n",cont+1,lista[cont],d);
		}
		
	return 0;	
}
