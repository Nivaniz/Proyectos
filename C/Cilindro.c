#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc,char*argv[]){
	const double PI=3.1416;
	float h,area,vol;
	float radio;
	
	printf("\n Dame el valor del Radio");
	scanf("%f",&radio);
	printf("\n Dame el valor de la Altura");
	scanf("%f",&h);
	area=2*3.1416*radio*(radio+h);
	vol=3.1416*pow(radio,2)*h;
	printf("\n El valor de Area es:%f",area);
	printf("\n El valor de Volumen es: %f",vol);
	
	return 0;
}
