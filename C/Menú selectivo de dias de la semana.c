#include <stdio.h>
#include <stdlib.h>

int main (int argc, char*argv[]){
	int Dia=0;

	printf("Dame el numero del dia a conocer:");
	scanf("%d",&Dia);
	switch(Dia){
		case 1:
			printf("LUNES");
			break;
		case 2:
			printf("MARTES");
			break;
		case 3:
			printf("MIERCOLES");
			break;
		case 4:
			printf("JUEVES");
			break;
		case 5:
			printf ("VIERNES");
			break;
		case 6:
			printf("SABADO");
			break;
		case 7:
			printf("DOMINGO");
		default:
			printf("NO EXISTE ESE DIA, NUMERO FUERA DEL RANGO");
			break;
	}
	printf("\n\n GRACIAS POR PONER NUMERO");
	
	return 0;
}
