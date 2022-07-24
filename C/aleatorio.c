#include <stdio.h>
#include <stdlib.h>

int main (void){
	int Limite,Cara,roll,frecuencia1=0,frecuencia2=0,frecuencia3=0,frecuencia4=0,frecuencia5=0,frecuencia6=0;
	printf("Dame el numero limite:");
	scanf("%d",&Limite);
	printf("\n\n");
	for(roll=1;roll<=Limite;roll++){
		Cara=1+rand()%6;
		switch (Cara){
			case 1:
				++frecuencia1;
				break;
			case 2:
				++frecuencia2;
				break;
			case 3:
				++frecuencia3;
				break;
			case 4:
				++frecuencia4;
				break;
			case 5:
				++frecuencia5;
				break;
			case 6:
				++frecuencia6;
				break;
				}//fin de switch	
	}//fin de for
	printf("\t\t\t%5s %14s\n", "Cara dado","Frecuencia");
	printf("\t\t\t\t1%13d\n", frecuencia1);
	printf("\t\t\t\t2%13d\n", frecuencia2);
	printf("\t\t\t\t3%13d\n", frecuencia3);
	printf("\t\t\t\t4%13d\n", frecuencia4);
	printf("\t\t\t\t5%13d\n", frecuencia5);
	printf("\t\t\t\t6%13d\n", frecuencia6);
	return 0;
}
