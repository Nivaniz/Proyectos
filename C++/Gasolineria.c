#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc,char*argv[]){
	
	float preciolitro,total,galonsurt;
	//GALON VALE 3.785
	printf("\n Dame los galones a surtir");
	scanf("%f",&galonsurt);
	printf("\n Dame el precio por litro");
	scanf("%f",&preciolitro);
	total=galonsurt*3.785*preciolitro;
	printf("\n El total a pagar es de:%f",total);
	return 0;
}
