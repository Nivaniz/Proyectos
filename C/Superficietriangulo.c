#include <stdio.h>

int main (){
	float base,altura,sup;
	
	printf ("Dame el valor de la Base");
	scanf("%f",&base);
	printf("Dame el valor de la altura");
	scanf("%f",&altura);
	sup=base*altura/2;
	printf("el resultado de la superficie es:%f",sup);
	return 0;
}
